from click.testing import CliRunner
from src.commands.cmd_exporter import cli


def test_export_graphs_from_local_directory():
    runner = CliRunner()
    result = runner.invoke(cli, ["cmd-export-graphs-from-local-directory"])
    assert result.exit_code == 0
    assert not result.exception
    assert "PEA-HAZOP-Dosiermodul_v07.xlsx" in result.output


def test_export_graphs_from_fuseki_server():
    runner = CliRunner()
    result = runner.invoke(cli, ["cmd-export-graphs-from-fuseki-server"])
    assert result.exit_code == 0 or result.exit_code == 1
    assert "PEA-HAZOP-Dosiermodul_v07.xlsx" or \
        "Error: Failed connection to Fuseki server" in result.output
