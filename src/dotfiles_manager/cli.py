from __future__ import annotations

from typing import TYPE_CHECKING

import click

from dotfiles_manager.subcommands.submodules import add
from dotfiles_manager.utils.dotfiles import Dotfiles

if TYPE_CHECKING:
    from click import Context


@click.group()
@click.pass_context
def cli(ctx: Context) -> None:
    """CRUD objects in your dotfiles in a beautiful manner."""
    ctx.obj = Dotfiles()


@cli.group()
@click.pass_obj
def submodules(ctx: Dotfiles) -> None:
    """Operate on your dotfiles' git submodules."""
    pass


submodules.add_command(add)
