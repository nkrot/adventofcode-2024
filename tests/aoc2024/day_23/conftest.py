import pytest
from tests.aoc2024.helpers import TData

from aoc2024 import day_23 as day

@pytest.fixture()
def tdata_1():
    return TData.from_module(day, "test.1.txt", 7,  "co,de,ka,ta")

@pytest.fixture()
def tdata_real():
    return TData.from_module(day, "input.txt", 1077, "bc,bf,do,dw,dx,ll,ol,qd,sc,ua,xc,yu,zt")
