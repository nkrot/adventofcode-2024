import pytest
from tests.aoc2024.helpers import TData

from aoc2024 import day_16 as day

@pytest.fixture()
def tdata_1():
    return TData.from_module(day, "test.1.txt", 7036, 45)

@pytest.fixture()
def tdata_2():
    return TData.from_module(day, "test.2.txt", 11048, 64)

@pytest.fixture()
def tdata_3():
    return TData.from_module(day, "test.3.txt", 2011, None)

@pytest.fixture()
def tdata_real():
    return TData.from_module(day, "input.txt", 94436, 481)
