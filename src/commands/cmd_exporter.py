import click
import glob
import os
import json

from src.services.svc_exporter import Service as service_exporter
from src.services.svc_triplestore import Service as service_triplestore
import src.excel_config.excel_config as config


class Context:
    """Context object which holds state for this particular invocation

    Attributes:
        svc_exporter (Service): Exporter business logic described as service
        svc_triplestore (Service): Triplestore business logic described as service
    """

    def __init__(self):
        self.svc_exporter = service_exporter()
        self.svc_triplestore = service_triplestore()


def export_graphs_from_fuseki_server(ctx):
    """Exports graphs from Fuseki server in excel format

    Args:
        ctx (Context): Context object

    Raises:
        click.ClickException: If connection to server failes
        click.ClickException: If no available data on the server
    """
    response = ctx.obj.svc_triplestore.get_dataset_information()

    if not bool(response):
        raise click.ClickException("Failed connection to Fuseki server")

    response_dict = json.loads(response)

    graphnames = []
    for bindings in response_dict["results"]["bindings"]:
        graphnames.append(bindings["g"]["value"])

    if not bool(graphnames):
        raise click.ClickException("There is no data on Fuseki server")

    for graphname in graphnames:
        graph = ctx.obj.svc_triplestore.get_hazop_graph(graphname)
        save_graph_in_data_excel_directory(ctx, graph, graphname)


def export_graphs_from_local_directory(ctx):
    """Exports graphs from local directory in excel format

    Args:
        ctx (Context): Context object

    Raises:
        click.ClickException: If no available data in local directory
    """
    graphpaths = ctx.obj.svc_exporter.read_turtle_data()

    if not bool(graphpaths):
        raise click.ClickException("There is no data in local directory")

    for graphpath in graphpaths:
        with open(graphpath, "r") as f:
            graph = f.read()

        graphname = os.path.split(graphpath)[1]
        save_graph_in_data_excel_directory(ctx, graph, graphname)


def save_graph_in_data_excel_directory(ctx, graph, graphname):
    """Saves graphs in data directory

    Args:
        ctx (Context): Context object
        graph (str): Graph in string format
        graphname (str): Name of the graph
    """
    graphname = graphname.replace(".ttl", ".xlsx")

    args = (ctx.obj.svc_exporter.parse_hazop_graph(graph),
            config.output_header,
            graphname)

    ctx.obj.svc_exporter.export_hazop_to_excel(args)
    click.echo("Saved file in data excel directory: {}".format(graphname))


@click.group()
@click.pass_context
def cli(ctx):
    """Exporter interface
    """
    ctx.obj = Context()


@cli.command()
@click.pass_context
def cmd_export_graphs_from_fuseki_server(ctx):
    """Export HAZOP graphs from Fuseki server
    """
    export_graphs_from_fuseki_server(ctx)


@cli.command()
@click.pass_context
def cmd_export_graphs_from_local_directory(ctx):
    """Export HAZOP graphs from local directory
    """
    export_graphs_from_local_directory(ctx)
