import pytest
from tests.aoc2024.helpers import TData

from aoc2024 import day_22 as day

@pytest.fixture()
def tdata_1():
    return TData.from_module(day, "test.1.txt", 37327623, None)

@pytest.fixture()
def tdata_2():
    return TData.from_module(day, "test.2.txt", None, 7+7+0+9)

@pytest.fixture()
def tdata_real():
    return TData.from_module(day, "input.txt", 20332089158, 2191)
