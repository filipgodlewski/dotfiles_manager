from __future__ import annotations

from typing import TYPE_CHECKING

import pytest
from click.testing import CliRunner

if TYPE_CHECKING:
    from typing import Callable

    from click.testing import Result


@pytest.fixture()
def invoke() -> Callable[..., Result]:
    runner: CliRunner = CliRunner()
    return runner.invoke
