from typing import Callable
from click.testing import Result

from dotfiles_manager.cli import cli

def test_can_call_cli(invoke: Callable[..., Result]) -> None:
    result: Result = invoke(cli)
    assert result.exit_code == 0


def test_call_to_inexistent_command_throws_error(invoke: Callable[..., Result]) -> None:
    result: Result = invoke(cli, ["wrong"])
    assert isinstance(result.exception, SystemExit)
    assert result.exit_code == 2
    assert "Error" in result.output


def test_can_call_submodules(invoke: Callable[..., Result]) -> None:
    result: Result = invoke(cli, ["submodules"])
    assert result.exit_code == 0
