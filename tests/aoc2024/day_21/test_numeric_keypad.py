import pytest

from aoc2024.day_21 import numeric_keypad as nkp

@pytest.mark.parametrize(
    "src, trg, expected", [
    ("A", "0", ["<A"]),
    ("2", "9", [">^^A", "^^>A", "^>^A"]),
    ("9", "A", ["vvvA"]),
])
def test_press(src, trg, expected):
    actual = nkp.press(src, trg)
    assert sorted(expected) == sorted(actual)

@pytest.mark.parametrize(
    "code, expected", [
    ("029A", ["<A^A>^^AvvvA", "<A^A^>^AvvvA", "<A^A^^>AvvvA"])
])
def test_type_code(code, expected):
    actual = nkp.type_code(code)
    assert sorted(expected) == sorted(actual)
