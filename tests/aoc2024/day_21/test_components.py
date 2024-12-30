"""
tests for some low level functions from solution.py
"""

import pytest

from aoc2024.day_21.solution import compute_code_complexity, type_code


@pytest.mark.parametrize(
    "code,sequence,expected", [
    ("029A", "<vA<AA>>^AvAA<^A>A<v<A>>^AvA^A<vA>^A<v<A>^A>AAvA^A<v<A>A>^AAAvA<^A>A", 68*29),
    ("980A", 60, 60 * 980),
])
def test_compute_code_complexity(code, sequence, expected):
    assert expected == compute_code_complexity(code, sequence)


@pytest.mark.parametrize(
    "code, expected", [
    ("029A", "<vA<AA>>^AvAA<^A>A<v<A>>^AvA^A<vA>^A<v<A>^A>AAvA^A<v<A>A>^AAAvA<^A>A"),
    ("980A", "<v<A>>^AAAvA^A<vA<AA>>^AvAA<^A>A<v<A>A>^AAAvA<^A>A<vA>^A<A>A"),
])
def test_type_code(code, expected):
    actual = type_code(code)
    assert expected in actual
