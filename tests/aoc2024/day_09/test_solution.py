
import pytest

from aoc2024.day_09.solution import solve_p1, solve_p2, parse_line, compute_checksum

def test_parse_line_1():
    expected = [
        [ 0, 1],
        [-1, 2],
        [ 1, 3],
        [-1, 4],
        [ 2, 5],
    ]
    actual = parse_line("12345")
    assert expected == actual

def test_parse_line_2():
    expected = [
        [ 0, 9],
        [-1, 0],
        [ 1, 9],
        [-1, 0],
        [ 2, 9],
    ]
    actual = parse_line("90909")
    assert expected == actual


def test_compute_checksum():
    disk = [[0, 2], [9, 2], [8, 1]]  # 00998
    actual = compute_checksum(disk)
    expected = sum([0 * 0, 1 * 0, 2 * 9, 3 * 9, 4 * 8]) # 77
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
