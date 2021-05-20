import click, glob, os

from src.services.svc_importer import Service
from src.config.config import config


class Context:
    def __init__(self):
        self.service = Service()
        self.excel_data = None
        self.hazop_data = None
        self.rdf_graphs = None


def list_excel_data(ctx):
    excel_data_path = ctx.obj.service.read_excel_data()

    if not bool(excel_data_path):
        raise click.ClickException("No Excel data found")

    ctx.obj.excel_data = []

    click.echo("Excel data list:")

    for path in excel_data_path:
        filename = path.replace("data/", "")
        ctx.obj.excel_data.append(filename)
        click.echo(filename)


def read_hazop_data(ctx):
    list_excel_data(ctx)

    ctx.obj.hazop_data = []

    for filename in ctx.obj.excel_data:
        if filename == config["HAZOP"]["filename"]:
            engine     = config["HAZOP"]["engine"]
            header     = config["HAZOP"]["header"]
            sheet_name = config["HAZOP"]["sheet_name"]

            filepath = os.path.join("data", filename)
            df = ctx.obj.service.read_hazop_data(filepath,
                                                 engine,
                                                 header,
                                                 sheet_name)
            df.name = filename
            ctx.obj.hazop_data.append(df)
        else:
            click.echo("Missed config for {}".format(filename))

    if not bool(ctx.obj.hazop_data):
        raise click.ClickException("No HAZOP data found")

    click.echo("Number of HAZOP files: {}".format(len(ctx.obj.hazop_data)))


def make_rdf_graphs(ctx):
    read_hazop_data(ctx)

    ctx.obj.rdf_graphs = {}

    for df in ctx.obj.hazop_data:
        graph = ctx.obj.service.make_rdf_graph(df)
        graph_name = df.name.replace(".xlsb", ".ttl")
        ctx.obj.rdf_graphs[graph_name] = graph

        save_graph_locally(graph, graph_name)
        # upload_graph_to_fuseki(graph, graph_name)
        echo_graphs_info(ctx)


def echo_graphs_info(ctx):
    number_of_triples = 0

    for k, v in ctx.obj.rdf_graphs.items():
        number_of_triples += len(v)

    click.echo("Number of RDF-Graphs: {}".format(len(ctx.obj.rdf_graphs)))
    click.echo("Nubmer of Triples: {}".format(number_of_triples))


def save_graph_locally(graph, graph_name):
    graph_str = graph.serialize(format="turtle").decode("utf-8")
    pathname = os.path.join("data/turtle", graph_name)

    with open(pathname, "w") as file:
        file.write(graph_str)


# # def upload_graph_to_fuseki(graph):
# #     ctx.obj.triplestore_service.upload(graph)


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
def cmd_make_rdf_graphs(ctx):
    """Make RDF-Graphs"""
    make_rdf_graphs(ctx)
