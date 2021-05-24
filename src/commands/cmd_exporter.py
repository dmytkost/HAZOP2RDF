import click
import os
import glob
import json

from src.services.svc_exporter import Service as service_exporter
from src.services.svc_triplestore import Service as service_triplestore
from src.config.config import config


class Context:
    def __init__(self):
        self.svc_exporter = service_exporter()
        self.svc_triplestore = service_triplestore()


def export_graphs_from_fuseki_server(ctx):
    response = ctx.obj.svc_triplestore.get_hazop_graph_bindings()

    if not bool(response):
        raise click.ClickException("Failed connection to Fuseki server")

    response_dict = json.loads(response)

    list_of_graphs = []
    for graph in response_dict["results"]["bindings"]:
        list_of_graphs.append(graph["g"]["value"])

    if not bool(list_of_graphs):
        raise click.ClickException("There is no data in Fuseki server")

    for filename in list_of_graphs:
        graph = ctx.obj.svc_triplestore.get_hazop_graph(filename)
        save_graph_in_data_excel_directory(ctx, graph, filename)


def export_graphs_from_local_directory(ctx):
    list_of_graphs = ctx.obj.svc_exporter.read_turtle_data()

    if not bool(list_of_graphs):
        raise click.ClickException("There is no data in local directory")

    for filepath in list_of_graphs:
        with open(filepath, "r") as f:
            graph = f.read()

        filename = os.path.split(filepath)[1]
        save_graph_in_data_excel_directory(ctx, graph, filename)


def save_graph_in_data_excel_directory(ctx, graph, filename):
    index = config["HAZOP"]["new_multiindex"]
    graph_parsed = ctx.obj.svc_exporter.parse_graph(graph)
    df = ctx.obj.svc_exporter.create_hazop_dataframe(graph_parsed, index)
    df.name = filename.replace(".ttl", ".xlsx")
    ctx.obj.svc_exporter.export_to_excel(df)
    click.echo("Saved file in data excel directory: {}".format(df.name))


@click.group()
@click.pass_context
def cli(ctx):
    """Exporter interface for RDF-Graphs"""
    ctx.obj = Context()


@cli.command()
@click.pass_context
def cmd_export_graphs_from_fuseki_server(ctx):
    """Export RDF-Graphs from Fuseki server"""
    export_graphs_from_fuseki_server(ctx)


@cli.command()
@click.pass_context
def cmd_export_graphs_from_local_directory(ctx):
    """Export RDF-Graphs from local directory"""
    export_graphs_from_local_directory(ctx)
