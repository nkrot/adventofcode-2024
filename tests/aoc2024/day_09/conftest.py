import pytest
from tests.aoc2024.helpers import TData

from aoc2024 import day_09 as day

@pytest.fixture()
def tdata_1():
    return TData.from_module(day, "test.1.txt", 1928, 2858)

@pytest.fixture()
def tdata_real():
    return TData.from_module(day, "input.txt", 6291146824486, 6307279963620)
