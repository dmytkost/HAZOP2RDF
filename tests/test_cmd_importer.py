from click.testing import CliRunner
from src.commands.cmd_importer import cli


def test_list_excel_data():
    runner = CliRunner()
    result = runner.invoke(cli, ["cmd-list-excel-data"])
    assert result.exit_code == 0
    assert not result.exception
    assert "PEA-HAZOP-Dosiermodul_v07.xlsb" in result.output


def test_read_hazop_data():
    runner = CliRunner()
    result = runner.invoke(cli, ["cmd-read-hazop-data"])
    assert result.exit_code == 0
    assert not result.exception
    assert "Number of files with HAZOP config: 1" in result.output


def test_build_hazop_graphs():
    runner = CliRunner()
    result = runner.invoke(cli, ["cmd-build-hazop-graphs"])
    assert result.exit_code == 0 or result.exit_code == 1
    assert "Nubmer of Triples: 480" in result.output
    assert "data/turtle/PEA-HAZOP-Dosiermodul_v07.ttl" in result.output
