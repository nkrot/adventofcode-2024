import pytest
from tests.aoc2024.helpers import TData

from aoc2024 import day_12 as day

@pytest.fixture()
def tdata_1():
    return TData.from_module(
        day,
        "test.1.txt",
        140,  # 4 * 10 + 4 * 8 + 4 * 10 + 1 * 4 + 3 * 8
        80,   # 16 + 16 + 32 + 4 + 12
    )

@pytest.fixture()
def tdata_2():
    return TData.from_module(
        day,
        "test.2.txt",
        772, # 756 + 4 + 4 + 4 + 4
        436,
    )

@pytest.fixture()
def tdata_3():
    return TData.from_module(day, "test.3.txt", 1930, 1206)

@pytest.fixture()
def tdata_4():
    return TData.from_module(day, "test.4.txt", None, 236)

@pytest.fixture()
def tdata_5():
    return TData.from_module(day, "test.5.txt", None, 368)

@pytest.fixture()
def tdata_real():
    return TData.from_module(day, "input.txt", 1377008, 815788)
