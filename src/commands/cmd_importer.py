import click
import glob
import os

from src.services.svc_importer import Service as service_importer
from src.services.svc_triplestore import Service as service_triplestore
import src.config.config as config


class Context:
    """Context object which holds state for this particular invocation

    Attributes:
        svc_importer (Service): Importer business logic described as Service
        svc_triplestore (Service): Triplestore business logic described as Service
    """

    def __init__(self):
        self.svc_importer = service_importer()
        self.svc_triplestore = service_triplestore()


def read_excel_data(ctx):
    """Reads excel data from data directory

    Args:
        ctx (Context): Context object

    Returns:
        list: List of excel data

    Raises:
        click.ClickException: If no excel data found
    """
    list_of_excel_data = ctx.obj.svc_importer.read_excel_data()

    if not bool(list_of_excel_data):
        raise click.ClickException("No excel data found")

    click.echo("List of Excel data: {}".format(list_of_excel_data))

    return list_of_excel_data


def read_hazop_data(ctx):
    """Reads and validates HAZOP data

    Args:
        ctx (Context): Context object

    Returns:
        list: List of HAZOP data

    Raises:
        click.ClickException: If no valid HAZOP data found
    """
    list_of_excel_data = read_excel_data(ctx)
    list_of_hazop_data = {}

    for filepath in list_of_excel_data:
        filename = os.path.split(filepath)[1]

        if not filename in config.excel_binary["files"]:
            click.echo("Missed config for {}".format(filename))
            continue

        engine = config.excel_binary["engine"]
        header = config.excel_binary["header"]
        sheet_name = config.excel_binary["sheet_name"]

        df = ctx.obj.svc_importer.read_hazop_data(filepath,
                                                  engine,
                                                  header,
                                                  sheet_name)

        is_valid = df.columns.tolist() == config.excel_binary["old_multiindex"]

        if not bool(is_valid):
            click.echo("HAZOP data does not match the scheme")
            continue

        list_of_hazop_data[filename] = df

    if not bool(list_of_hazop_data):
        raise click.ClickException("No HAZOP data found")

    click.echo(f"Number of files with HAZOP config: {len(list_of_hazop_data)}")

    return list_of_hazop_data


def build_hazop_graphs(ctx):
    """Builds HAZOP graphs, saves it locally and uploads to Fuseki server

    Args:
        ctx (Context): Context object
    """
    list_of_hazop_data = read_hazop_data(ctx)

    for key, val in list_of_hazop_data.items():
        graph = ctx.obj.svc_importer.build_hazop_graph(val)
        filename = key.replace(".xlsb", ".ttl")
        filepath = os.path.join("data", "turtle", filename)

        save_graph_locally(graph, filepath)

    for key, val in list_of_hazop_data.items():
        graph = ctx.obj.svc_importer.build_hazop_graph(val)
        filename = key.replace(".xlsb", ".ttl")
        filepath = os.path.join("data", "turtle", filename)

        upload_graph_to_fuseki(ctx, filename, filepath)


def save_graph_locally(graph, filepath):
    """Saves graph locally

    Args:
        graph (str): Graph in string format
        filepath (str): Path of the file
    """
    with open(filepath, "w") as file:
        file.write(graph)

    click.echo("Saved file in data turtle directory: {}".format(filepath))


def upload_graph_to_fuseki(ctx, filename, filepath):
    """Uploads graph to Fuseki server

    Args:
        ctx (Context): Context object
        filename (str): Name of the file
        filepath (str): Path of the file

    Raises:
        click.ClickException: If Fuseki server is offline
    """
    response = ctx.obj.svc_triplestore.upload_hazop_graph(filename, filepath)

    if response != 0:
        raise click.ClickException("Failed connection to Fuseki server")

    click.echo("Uploaded file to Fuseki server: {}".format(filename))


@click.group()
@click.pass_context
def cli(ctx):
    """Importer interface
    """
    ctx.obj = Context()


@cli.command()
@click.pass_context
def cmd_read_excel_data(ctx):
    """Read excel data
    """
    read_excel_data(ctx)


@cli.command()
@click.pass_context
def cmd_read_hazop_data(ctx):
    """Read hazop data
    """
    read_hazop_data(ctx)


@cli.command()
@click.pass_context
def cmd_build_hazop_graphs(ctx):
    """Build HAZOP graphs
    """
    build_hazop_graphs(ctx)
