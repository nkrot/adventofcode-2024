import pytest
from tests.aoc2024.helpers import TData

from aoc2024 import day_11 as day

@pytest.fixture()
def tdata_1():
    return TData.from_module(day, "test.1.txt", 55312, 65601038650482)

@pytest.fixture()
def tdata_real():
    return TData.from_module(day, "input.txt", 202019, 239321955280205)
