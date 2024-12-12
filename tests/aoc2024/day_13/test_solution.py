
import pytest

from aoc2024.day_13.solution import solve_p1, solve_p2, compute, compute_with_numpy

@pytest.mark.parametrize(
    "m,expected", [
    ([[94, 34], [22, 67], [8400, 5400]], 280),
    ([[70, 17], [23, 22], [4074, 2598]], 176),
    ([[11, 40], [82, 40], [8155, 7280]], 0)
])
def test_compute(m, expected):
    assert expected == compute(m)

@pytest.mark.parametrize(
    "m,expected", [
    ([[94, 34], [22, 67], [8400, 5400]], 280),
    ([[70, 17], [23, 22], [4074, 2598]], 176),
    ([[11, 40], [82, 40], [8155, 7280]], 0)
])
def test_compute_with_numpy(m, expected):
    assert expected == compute_with_numpy(m)

def test_solve_p1(tdata_1):
    actual = solve_p1(tdata_1.path)
    assert tdata_1.expected_p1 == actual

# def test_solve_p2(tdata_1):
#     actual = solve_p2(tdata_1.path)
#     assert tdata_1.expected_p2 == actual

def test_solve_p1_real(tdata_real):
    actual = solve_p1(tdata_real.path)
    assert tdata_real.expected_p1 == actual

def test_solve_p2_real(tdata_real):
    actual = solve_p2(tdata_real.path)
    assert tdata_real.expected_p2 == actual
