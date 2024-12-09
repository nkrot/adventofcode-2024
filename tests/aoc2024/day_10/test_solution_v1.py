import pytest

from aoc2024.day_10.solution import solve_p1_v1

def test_solve_p1_v1(tdata_1):
    actual = solve_p1_v1(tdata_1.path)
    assert tdata_1.expected_p1 == actual

def test_solve_p1_v1_real(tdata_real):
    actual = solve_p1_v1(tdata_real.path)
    assert tdata_real.expected_p1 == actual
