from __future__ import annotations

from os.path import join
from typing import TYPE_CHECKING

import click

if TYPE_CHECKING:
    from typing import Tuple

    from dotfiles_manager.utils.dotfiles import Dotfiles


@click.command()
@click.option("--folder", "-f", help="folder to add submodule to", required=True)
# type=click.Choice([d for d in ctx.DIRS], case_sensitive=True))
@click.argument("target")
@click.pass_obj
def add(ctx: Dotfiles, folder: str, target: str) -> None:
    """Add new submodule under specified directory in your dotfiles."""
    if folder not in ctx.DIRS:
        raise KeyError(f"{folder} not in dirs. Use `--help` flag for more information")
    url, name, relative_path = get_submodule_info(ctx, folder, target)
    ctx.repo.create_submodule(name=relative_path, path=relative_path, url=url)
    click.secho("\nAdded new submodule.\n", fg="green")
    click.secho(f"Name: {name}", fg="yellow")
    click.echo(f"Path: {relative_path}")
    click.echo(f"URL: {url}")
    ctx.repo.submodule_update(recursive=True, force_remove=True, init=True, force_reset=True)
    click.secho("\nUpdated recursively all submodules.", fg="green")


def get_submodule_info(ctx: Dotfiles, folder: str, target: str) -> Tuple[str, str, str]:
    """Gets necessary Github information based on the repository name and end dir."""

    cleaned_target: str = target[:-1] if target.endswith(ctx.GH_OBJECT + "/") else target
    is_gh_domain: bool = cleaned_target.startswith(ctx.GH_DOMAIN)
    is_gh_object: bool = cleaned_target.endswith(ctx.GH_OBJECT)
    if is_gh_domain and is_gh_object:
        url: str = cleaned_target
    elif is_gh_object:
        url: str = ctx.GH_DOMAIN + cleaned_target
    else:
        url: str = ctx.GH_DOMAIN + cleaned_target + ctx.GH_OBJECT
    name: str = cleaned_target.split("/")[-1]
    name: str = name[:-4] if is_gh_object else name
    relative_path: str = join(folder, ".local", join(ctx.DIRS[folder], name))
    return url, name, relative_path
