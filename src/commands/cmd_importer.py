import click, glob, os

from src.services.svc_importer import Service as service_importer
from src.services.svc_triplestore import Service as service_triplestore
from src.config.config import config


class Context:
    def __init__(self):
        self.svc_importer = service_importer()
        self.svc_triplestore = service_triplestore()
        self.excel_data = None
        self.hazop_data = None
        self.rdf_graphs = None


def list_excel_data(ctx):
    list_of_excel_data = ctx.obj.svc_importer.read_excel_data()

    if not bool(list_of_excel_data):
        raise click.ClickException("No Excel data found")

    ctx.obj.excel_data = []

    click.echo("Excel data list:")

    for path in list_of_excel_data:
        filename = os.path.split(path)[1]
        ctx.obj.excel_data.append(filename)
        click.echo(filename)


def read_hazop_data(ctx):
    list_excel_data(ctx)

    ctx.obj.hazop_data = []
    for filename in ctx.obj.excel_data:
        if filename in config["HAZOP"]["files"]:
            engine     = config["HAZOP"]["engine"]
            header     = config["HAZOP"]["header"]
            sheet_name = config["HAZOP"]["sheet_name"]

            filepath = os.path.join("data", filename)
            df = ctx.obj.svc_importer.read_hazop_data(filepath,
                                                      engine,
                                                      header,
                                                      sheet_name)
            df.name = filename
            validator = (set(df.columns.tolist()) == set(
                config["HAZOP"]["old_multiindex"]))

            if bool(validator):
                ctx.obj.hazop_data.append(df)
            else:
                click.echo("HAZOP data does not match the schema")
        else:
            click.echo("Missed config for {}".format(filename))
    if not bool(ctx.obj.hazop_data):
        raise click.ClickException("No HAZOP data found")

    click.echo(f"Number of files with HAZOP config: {len(ctx.obj.hazop_data)}")


def build_hazop_graphs(ctx):
    read_hazop_data(ctx)

    ctx.obj.rdf_graphs = {}

    for df in ctx.obj.hazop_data:
        graph = ctx.obj.svc_importer.build_hazop_graph(df)
        filename = df.name.replace(".xlsb", ".ttl")
        filepath = os.path.join("data", "turtle", filename)

        ctx.obj.rdf_graphs[filename] = graph

        hazop_build_info(ctx)
        save_graph_locally(graph, filepath)
        upload_graph_to_fuseki(ctx, filename, filepath)


def hazop_build_info(ctx):
    number_of_triples = 0

    for k, v in ctx.obj.rdf_graphs.items():
        number_of_triples += len(v)

    click.echo("Nubmer of Triples: {}".format(number_of_triples))


def save_graph_locally(graph, filepath):
    graph_str = graph.serialize(format="turtle").decode("utf-8")

    with open(filepath, "w") as file:
        file.write(graph_str)

    click.echo("Saved file in data turtle directory: {}".format(filepath))


def upload_graph_to_fuseki(ctx, filename, filepath):
    response = ctx.obj.svc_triplestore.upload_hazop_graph(filename, filepath)

    if response != 0:
        raise click.ClickException("Failed connection to Fuseki server")

    click.echo("Uploaded file to Fuseki server: {}".format(filename))


@click.group()
@click.pass_context
def cli(ctx):
    """Entry point for reading data and making RDF-Graphs"""
    ctx.obj = Context()


@cli.command()
@click.pass_context
def cmd_list_excel_data(ctx):
    """List Excel data"""
    list_excel_data(ctx)


@cli.command()
@click.pass_context
def cmd_read_hazop_data(ctx):
    """Read HAZOP data"""
    read_hazop_data(ctx)


@cli.command()
@click.pass_context
def cmd_build_hazop_graphs(ctx):
    """Make RDF-Graphs"""
    build_hazop_graphs(ctx)
