
import pytest

from aoc2024.day_22.solution import solve_p1, solve_p2, get_secret_number


def test_get_secret_number_1():
    secret = 123
    expected = [15887950, 16495136, 527345, 704524, 1553684, 12683156,
                11100544, 12249484, 7753432, 5908254]

    actual = []
    for _ in range(len(expected)):
        secret = get_secret_number(secret)
        actual.append(secret)

    assert expected == actual

def test_solve_p1(tdata_1):
    actual = solve_p1(tdata_1.path)
    assert tdata_1.expected_p1 == actual

def test_solve_p2(tdata_2):
    actual = solve_p2(tdata_2.path)
    assert tdata_2.expected_p2 == actual

def test_solve_p1_real(tdata_real):
    actual = solve_p1(tdata_real.path)
    assert tdata_real.expected_p1 == actual

def test_solve_p2_real(tdata_real):
    actual = solve_p2(tdata_real.path)
    assert tdata_real.expected_p2 == actual
