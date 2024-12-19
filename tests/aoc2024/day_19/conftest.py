import pytest
from tests.aoc2024.helpers import TData

from aoc2024 import day_19 as day

@pytest.fixture()
def tdata_1():
    return TData.from_module(day, "test.1.txt", 6, 16)

@pytest.fixture()
def tdata_real():
    return TData.from_module(day, "input.txt", 317, 883443544805484)
