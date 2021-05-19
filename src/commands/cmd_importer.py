import click, glob

from src.services.svc_importer import Service


class Context:
    def __init__(self):
        self.service = Service()


@click.group()
@click.pass_context
def cli(ctx):
    """Entry point for reading data and making RDF-Graphs"""
    ctx.obj = Context()


@cli.command()
@click.pass_context
def list_excel_data(ctx):
    """List Excel data"""
    excel_data = ctx.obj.service.read_excel_data()
    if bool(excel_data):
        for filename in excel_data:
            click.echo(filename)
    else:
        raise click.ClickException("No Excel data found")


@cli.command()
@click.pass_context
def read_hazop_data(ctx):
    """Read HAZOP data"""
    excel_data = ctx.obj.service.read_excel_data()
    if bool(excel_data):
        hazop_data = ctx.obj.service.read_hazop_data(excel_data)
        if bool(hazop_data):
            click.echo("Number of HAZOP files: {}".format(len(hazop_data)))
        else:
            raise click.ClickException("No HAZOP data found")
    else:
        raise click.ClickException("No Excel data found")


@cli.command()
@click.pass_context
def make_rdf_graphs(ctx):
    """Make RDF-Graphs"""
    excel_data = ctx.obj.service.read_excel_data()
    if bool(excel_data):
        hazop_data = ctx.obj.service.read_hazop_data(excel_data)
        if bool(hazop_data):
            rdf_graphs = ctx.obj.service.make_rdf_graphs(hazop_data)
            click.echo("Number of RDF-Graphs: {}".format(len(rdf_graphs)))
        else:
            raise click.ClickException("No HAZOP data found")
    else:
        raise click.ClickException("No Excel data found")
