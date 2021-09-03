from __future__ import annotations

from typing import TYPE_CHECKING

from dotfiles_manager.cli import cli

if TYPE_CHECKING:
    from typing import Callable

    from click.testing import Result


def test_calling_add_without_target_throws_an_error(invoke: Callable[..., Result]) -> None:
    result: Result = invoke(cli, ["submodules", "add"])

    assert isinstance(result.exception, SystemExit)
    assert result.exit_code == 2
    assert "Error" in result.output
