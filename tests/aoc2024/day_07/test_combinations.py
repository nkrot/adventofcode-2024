
from aoc2024.day_07.solution_v1 import combinations


def test_combinations_1():
    expected = [
        ('A', 'A', 'A'),
        ('A', 'A', 'B'),
        ('A', 'B', 'A'),
        ('A', 'B', 'B'),
        ('B', 'A', 'A'),
        ('B', 'A', 'B'),
        ('B', 'B', 'A'),
        ('B', 'B', 'B')
    ]

    actual = list(combinations('AB', 3))

    assert sorted(expected) == sorted(actual)


def test_combinations_no_duplicates():
    actual = list(combinations('AB', 4))

    assert len(actual) == len(set(actual))
