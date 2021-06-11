from click.testing import CliRunner
from src.cli import cli


def test_cli():
    """Test CLI to import all commands without any error and exception
    """
    runner = CliRunner()
    result = runner.invoke(cli)
    assert result.exit_code == 0
    assert not result.exception
