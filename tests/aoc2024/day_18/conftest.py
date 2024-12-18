import pytest
from tests.aoc2024.helpers import TData

from aoc2024 import day_18 as day

@pytest.fixture()
def tdata_1():
    return TData.from_module(day, "test.1.txt", 22, "6,1")

@pytest.fixture()
def tdata_real():
    return TData.from_module(day, "input.txt", 246, "22,50")
