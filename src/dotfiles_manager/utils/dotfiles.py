from __future__ import annotations

from os.path import expanduser, join
from typing import TYPE_CHECKING

from git import Repo

if TYPE_CHECKING:
    from typing import Dict


class Dotfiles:
    DOTFILES_PATH: str = join(expanduser("~"), "dotfiles")
    DIRS: Dict[str, str] = {
        "alacritty": "share/alacritty",
        "nvim": "share/nvim/site/pack/plugins/start",
        "tmux": "share/tmux",
        "zsh": "share/zsh/plugins",
        "other": "share/other",
    }
    GH_DOMAIN = "https://github.com/"
    GH_OBJECT = ".git"

    def __init__(self) -> None:
        self.repo: Repo = Repo(self.DOTFILES_PATH)
