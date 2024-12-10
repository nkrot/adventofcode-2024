import pytest
from tests.aoc2024.helpers import TData

from aoc2024 import day_03 as day

@pytest.fixture()
def tdata_1():
    return TData.from_module(day, "test.1.txt", 161, -1)

@pytest.fixture()
def tdata_2():
    return TData.from_module(day, "test.2.txt", -1, 48)

@pytest.fixture()
def tdata_real():
    return TData.from_module(day, "input.txt", 175615763, 74361272)
