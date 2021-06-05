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
        list: Excel data list

    Raises:
        click.ClickException: If no Excel data found
    """
    excel_data_list = ctx.obj.svc_importer.read_excel_data()

    if not bool(excel_data_list):
        raise click.ClickException("No Excel data found")

    click.echo("Excel data list: {}".format(excel_data_list))

    return excel_data_list


def read_hazop_data(ctx):
    """Reads and validates HAZOP data

    Args:
        ctx (Context): Context object

    Returns:
        dict: key - HAZOP dataframe path, value - HAZOP dataframe

    Raises:
        click.ClickException: If no valid HAZOP data found
    """
    excel_data_list = read_excel_data(ctx)
    hazop_data_list = {}

    for filepath in excel_data_list:
        _, suffix = os.path.splitext(filepath)

        args = (filepath,
                config.excel[suffix]["engine"],
                config.excel[suffix]["header"],
                config.excel[suffix]["sheet_name"])

        df = ctx.obj.svc_importer.get_hazop_dataframe(args)
        is_valid = df.columns.tolist() == config.excel[suffix]["valid_header"]

        if not bool(is_valid):
            click.echo("There is no valid header for {}".format(filepath))
            continue

        hazop_data_list[filepath] = df

    if not bool(hazop_data_list):
        raise click.ClickException("No HAZOP data found")

    click.echo(f"Number of files with HAZOP config: {len(hazop_data_list)}")

    return hazop_data_list


def build_hazop_graphs(ctx):
    """Builds HAZOP graphs, saves it locally and uploads to Fuseki server

    Args:
        ctx (Context): Context object
    """
    hazop_data_list = read_hazop_data(ctx)

    for df_path, df in hazop_data_list.items():
        graph = ctx.obj.svc_importer.build_hazop_graph(df)

        head, tail = os.path.split(df_path)
        _, suffix = os.path.splitext(tail)

        filename = tail.replace(suffix, ".ttl")
        filepath = os.path.join(head, "turtle", filename)

        save_graph_locally(graph, filepath)
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
    """
    response = ctx.obj.svc_triplestore.upload_hazop_graph(filename, filepath)

    if response == 0:
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
