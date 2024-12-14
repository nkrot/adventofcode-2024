import pytest
from tests.aoc2024.helpers import TData

from aoc2024 import day_15 as day

@pytest.fixture()
def tdata_1():
    return TData.from_module(day, "test.1.txt", 2028, None)

@pytest.fixture()
def tdata_2():
    return TData.from_module(day, "test.2.txt", 10092, 9021)

@pytest.fixture()
def tdata_3():
    return TData.from_module(day, "test.3.txt", None, 618)

@pytest.fixture()
def tdata_real():
    return TData.from_module(day, "input.txt", 1538871, None)
