import click, glob

from src.services.svc_exporter import Service as service_exporter
from src.services.svc_triplestore import Service as service_triplestore
from src.config.config import config


class Context:
    def __init__(self):
        self.svc_exporter = service_exporter()
        self.svc_triplestore = service_triplestore()


def export_rdf_graphs_from_fuseki_server(ctx):
    list_of_graphs = ctx.obj.svc_triplestore.get_hazop_graph_bindings()

    if not bool(list_of_graphs):
        raise click.ClickException("There is no data in Fuseki server")

    for filename in list_of_graphs:
        graph = ctx.obj.svc_triplestore.get_hazop_graph(filename)

        index = config["HAZOP"]["new_index"]
        filename = filename.replace(".ttl", ".xlsx")
        df_graph = ctx.obj.svc_exporter.create_hazop_dataframe(graph, index)
        ctx.obj.svc_exporter.export_to_excel(df_graph, filename)
        click.echo("Saved file in data/excel directory: {}".format(filename))


def export_rdf_graphs_from_local_directory(ctx):
    list_of_graphs = ctx.obj.svc_exporter.read_local_directory()

    if not bool(list_of_graphs):
        raise click.ClickException("There is no data in local directory")

    for filepath in list_of_graphs:
        with open(filepath, "r") as f:
            graph = f.read()

        index = config["HAZOP"]["new_index"]
        filename = filepath.replace("data/turtle/", "").replace(".ttl", ".xlsx")
        df_graph = ctx.obj.svc_exporter.create_hazop_dataframe(graph, index)
        ctx.obj.svc_exporter.export_to_excel(df_graph, filename)
        click.echo("Saved file in data/excel directory: {}".format(filename))


@click.group()
@click.pass_context
def cli(ctx):
    """Exporter interface for RDF-Graphs"""
    ctx.obj = Context()


@cli.command()
@click.pass_context
def cmd_export_rdf_graphs_from_fuseki_server(ctx):
    """Export RDF-Graphs"""
    export_rdf_graphs_from_fuseki_server(ctx)


@cli.command()
@click.pass_context
def cmd_export_rdf_graphs_from_local_directory(ctx):
    """Export RDF-Graphs"""
    export_rdf_graphs_from_local_directory(ctx)
