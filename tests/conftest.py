from typing import Callable

import pytest
from click.testing import CliRunner


@pytest.fixture
def invoke() -> Callable:
    runner: CliRunner = CliRunner()
    return runner.invoke
