
import pytest

from aoc2024.day_20.solution import solve_p1, solve_p2

def test_solve_p1(tdata_1):
    actual = solve_p1(tdata_1.path, 1)
    assert tdata_1.expected_p1 == actual

@pytest.mark.xfail(reason="Not solved yet")
def test_solve_p2(tdata_1):
    actual = solve_p2(tdata_1.path)
    assert tdata_1.expected_p2 == actual

def test_solve_p1_real(tdata_real):
    actual = solve_p1(tdata_real.path)
    assert tdata_real.expected_p1 == actual

@pytest.mark.xfail(reason="Not solved yet")
def test_solve_p2_real(tdata_real):
    actual = solve_p2(tdata_real.path)
    assert tdata_real.expected_p2 == actual
