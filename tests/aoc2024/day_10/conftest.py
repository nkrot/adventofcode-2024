import pytest
from tests.aoc2024.helpers import TData

from aoc2024 import day_10 as day

@pytest.fixture()
def tdata_1():
    return TData.from_module(day, "test.1.txt", 36, 81)

@pytest.fixture()
def tdata_real():
    return TData.from_module(day, "input.txt", 794, 1706)
