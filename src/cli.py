import click
import os


class ComplexCLI(click.MultiCommand):
    """Complex is an example of building very complex cli applications
    that load subcommands dynamically from a plugin folder and other things.

    All the commands are implemented as plugins in the `complex.commands`
    package. If a python module is placed named "cmd_foo" it will show up as
    "foo" command and the `cli` object within it will be loaded as nested
    Click command.

    Source: https://github.com/pallets/click/tree/main/examples/complex
    """

   def list_commands(self, ctx):
        commands = []
        commands_folder = os.path.abspath(
            os.path.join(os.path.dirname(__file__), "commands"))

        for filename in os.listdir(commands_folder):
            if filename.endswith(".py") and filename.startswith("cmd_"):
                commands.append(
                    filename.replace("cmd_", "").replace(".py", ""))

        commands.sort()

        return commands

    def get_command(self, ctx, name):
        try:
            mod = __import__(f"src.commands.cmd_{name}", None, None, ["cli"])
        except ImportError:
            return

        return mod.cli


@click.command(cls=ComplexCLI)
def cli():
    """Welcome to HAZOP CLI!"""
    pass
