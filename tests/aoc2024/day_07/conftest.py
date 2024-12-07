import pytest
from tests.aoc2024.helpers import TData

from aoc2024 import day_07

@pytest.fixture()
def tdata_1():
    return TData.from_module(day_07, "test.1.txt", 3749, 11387)

@pytest.fixture()
def tdata_real():
    return TData.from_module(day_07, "input.txt", 850435817339, 104824810233437)
