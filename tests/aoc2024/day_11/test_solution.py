
import pytest

from aoc2024.day_11.solution import solve_p1, solve_p2, evolve

@pytest.mark.parametrize(
    "stone,expected", [
    (0,   (1,)),
    (1,   (2024,)),
    (10,  (1, 0)),
    (99,  (9, 9)),
    (999, (2021976,))
])
def test_evolve(stone, expected):
    actual = evolve(stone)
    assert expected == actual

def test_solve_p1(tdata_1):
    actual = solve_p1(tdata_1.path)
    assert tdata_1.expected_p1 == actual

def test_solve_p2(tdata_1):
    actual = solve_p2(tdata_1.path)
    assert tdata_1.expected_p2 == actual

def test_solve_p1_real(tdata_real):
    actual = solve_p1(tdata_real.path)
    assert tdata_real.expected_p1 == actual

def test_solve_p2_real(tdata_real):
    actual = solve_p2(tdata_real.path)
    assert tdata_real.expected_p2 == actual
