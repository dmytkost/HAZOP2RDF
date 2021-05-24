import click
import glob
import os

from src.services.svc_importer import Service as service_importer
from src.services.svc_triplestore import Service as service_triplestore
from src.config.config import config


class Context:
    def __init__(self):
        self.svc_importer = service_importer()
        self.svc_triplestore = service_triplestore()


def list_excel_data(ctx):
    list_of_excel_data = ctx.obj.svc_importer.read_excel_data()

    if not bool(list_of_excel_data):
        raise click.ClickException("No Excel data found")

    click.echo("List of Excel data:")
    click.echo(*list_of_excel_data)

    return list_of_excel_data


def read_hazop_data(ctx):
    list_of_excel_data = list_excel_data(ctx)
    list_of_hazop_data = {}

    for filepath in list_of_excel_data:
        filename = os.path.split(filepath)[1]

        if filename in config["HAZOP"]["files"]:
            engine = config["HAZOP"]["engine"]
            header = config["HAZOP"]["header"]
            sheet_name = config["HAZOP"]["sheet_name"]

            df = ctx.obj.svc_importer.read_hazop_data(filepath,
                                                      engine,
                                                      header,
                                                      sheet_name)

            validator = (set(df.columns.tolist()) == set(
                config["HAZOP"]["old_multiindex"]))

            if bool(validator):
                list_of_hazop_data[filename] = df
            else:
                click.echo("HAZOP data does not match the schema")
        else:
            click.echo("Missed config for {}".format(filename))

    if not bool(list_of_hazop_data):
        raise click.ClickException("No HAZOP data found")

    click.echo(f"Number of files with HAZOP config: {len(list_of_hazop_data)}")

    return list_of_hazop_data


def build_hazop_graphs(ctx):
    list_of_hazop_data = read_hazop_data(ctx)

    for key, val in list_of_hazop_data.items():
        graph = ctx.obj.svc_importer.build_hazop_graph(val)
        filename = key.replace(".xlsb", ".ttl")
        filepath = os.path.join("data", "turtle", filename)

        save_graph_locally(graph, filepath)
        upload_graph_to_fuseki(ctx, filename, filepath)


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
