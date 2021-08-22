from os.path import expanduser, join
from typing import Dict

from git import Repo


class Dotfiles:
    DOTFILES_PATH = join(expanduser("~"), "dotfiles")
    DIRS: Dict[str, str] = {
        "alacritty": "share/alacritty",
        "nvim": "share/nvim/site/pack/plugins/start",
        "tmux": "share/tmux",
        "zsh": "share/zsh/plugins",
        "other": "share/other",
    }
    GH_DOMAIN = "https://github.com/"
    GH_OBJECT = ".git"

    def __init__(self):
        self.repo = Repo(self.DOTFILES_PATH)
