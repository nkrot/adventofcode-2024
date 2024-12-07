
import pytest

from aoc2024.day_07.solution_v1 import solve_p1, solve_p2


def test_solve_p1(tdata_1):
    actual = solve_p1(tdata_1.path)
    assert tdata_1.expected_p1 == actual


def test_solve_p2(tdata_1):
    actual = solve_p2(tdata_1.path)
    assert tdata_1.expected_p2 == actual

# running for real data not implemented because the solution is very slow
