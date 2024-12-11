
import pytest

from aoc2024.day_12.solution import solve_p1, solve_p2

def test_solve_p1_1(tdata_1):
    actual = solve_p1(tdata_1.path)
    assert tdata_1.expected_p1 == actual

def test_solve_p1_2(tdata_2):
    actual = solve_p1(tdata_2.path)
    assert tdata_2.expected_p1 == actual

def test_solve_p1_3(tdata_3):
    actual = solve_p1(tdata_3.path)
    assert tdata_3.expected_p1 == actual

def test_solve_p2_1(tdata_1):
    actual = solve_p2(tdata_1.path)
    assert tdata_1.expected_p2 == actual

def test_solve_p2_2(tdata_2):
    actual = solve_p2(tdata_2.path)
    assert tdata_2.expected_p2 == actual

def test_solve_p2_3(tdata_3):
    actual = solve_p2(tdata_3.path)
    assert tdata_3.expected_p2 == actual

def test_solve_p2_4(tdata_4):
    actual = solve_p2(tdata_4.path)
    assert tdata_4.expected_p2 == actual

def test_solve_p2_5(tdata_5):
    actual = solve_p2(tdata_5.path)
    assert tdata_5.expected_p2 == actual

def test_solve_p1_real(tdata_real):
    actual = solve_p1(tdata_real.path)
    assert tdata_real.expected_p1 == actual

def test_solve_p2_real(tdata_real):
    actual = solve_p2(tdata_real.path)
    assert tdata_real.expected_p2 == actual
