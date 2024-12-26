import pytest

from aoc2024 import matrix as m
from aoc2024.day_16.solution import Reindeer, move

@pytest.fixture
def deer():
    return Reindeer((13,1), m.LEFT, 0)


def test_move_1(deer):
    """move up and to the right"""
    deer = move(deer, (12,1))
    deer = move(deer, (11,1))
    deer = move(deer, (11,2))

    assert (11,2) == deer.xy
    assert m.RIGHT == deer.facing
    assert 2003 == deer.score


def test_move_2(deer):
    """move two steps to the right"""
    deer = move(deer, (13,2))
    deer = move(deer, (13,3))

    assert (13,3) == deer.xy
    assert m.RIGHT == deer.facing
    assert 1002 == deer.score
