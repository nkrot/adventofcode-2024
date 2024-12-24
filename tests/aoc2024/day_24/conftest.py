import pytest
from tests.aoc2024.helpers import TData

from aoc2024 import day_24 as day

@pytest.fixture()
def tdata_1():
    return TData.from_module(day, "test.1.txt", 4, None)

@pytest.fixture()
def tdata_2():
    return TData.from_module(day, "test.2.txt", 2024, None)

@pytest.fixture()
def tdata_real():
    return TData.from_module(day, "input.txt", 69201640933606, None)
