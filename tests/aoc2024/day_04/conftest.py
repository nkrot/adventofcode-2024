import pytest
from tests.aoc2024.helpers import TData

from aoc2024 import day_04 as day

@pytest.fixture()
def tdata_1():
    return TData.from_module(day, "test.1.txt", 18, 9)

@pytest.fixture()
def tdata_real():
    return TData.from_module(day, "input.txt", 2517, 1960)
