import pytest

from aoc2024.day_21 import directional_keypad as dkp

@pytest.mark.parametrize(
    "src, trg, expected", [
    ("A", "^", ["<A"]),
    ("A", "<", ["<v<A", "v<<A"]),
    ("<", "A", [">>^A", ">^>A"]),
])
def test_press(src, trg, expected):
    actual = dkp.press(src, trg)
    assert sorted(expected) == sorted(actual)

# "029A"
# ["<A^A>^^AvvvA", "<A^A^>^AvvvA", "<A^A^^>AvvvA"]
# v<<A>>^A<A>AvA<^AA>A<vAAA>^A

@pytest.mark.parametrize(
    "code, expected", [
    ("<A^A>^^AvvvA", "v<<A>>^A<A>AvA<^AA>A<vAAA>^A")
])
def test_type_code(code, expected):
    actual = dkp.type_code(code)
    # print(expected)
    # print(len(actual))
    # print("\n".join(actual))
    assert expected in actual
