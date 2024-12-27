import pytest
from tests.aoc2024.helpers import TData

from aoc2024 import day_17 as day

@pytest.fixture()
def tdata_1():
    return TData.from_module(day, "test.1.txt", "4,6,3,5,6,3,5,2,1,0", None)

@pytest.fixture()
def tdata_2():
    return TData.from_module(day, "test.2.txt", None, 117440)

@pytest.fixture()
def tdata_real():
    return TData.from_module(day, "input.txt", "1,5,7,4,1,6,0,3,0", None)
