from typing import Callable

import pytest
from click.testing import CliRunner, Result


@pytest.fixture
def invoke() -> Callable[..., Result]:
    runner: CliRunner = CliRunner()
    return runner.invoke
