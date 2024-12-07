
import pytest

from aoc2024 import matrix as m

@pytest.fixture()
def mat_3x2_str():
    return [
        ["1A", "1B"],
        ["2A", "2B"],
        ["3A", "3B"],
    ]

@pytest.fixture()
def mat_5x4_int():
    return [
        [0,1,2,3],
        [10,11,12,13],
        [20,21,22,23],
        [30,31,32,33],
        [40,41,42,43],
    ]


def test_shape_5x4(mat_5x4_int):
    assert (5, 4) == m.shape(mat_5x4_int)


def test_scan(mat_3x2_str):
    expected = [
        (0, 0), (0, 1),
        (1, 0), (1, 1),
        (2, 0), (2, 1)
    ]

    actual = list(m.scan(mat_3x2_str))

    assert expected == actual


def test_scan_with_value(mat_3x2_str):
    expected = [
        ((0, 0), "1A"), ((0, 1), "1B"),
        ((1, 0), "2A"), ((1, 1), "2B"),
        ((2, 0), "3A"), ((2, 1), "3B"),
    ]

    actual = list(m.scan(mat_3x2_str, with_value=True))

    assert expected == actual


def test_get_value_outside_of_matrix(mat_5x4_int):
    assert None == m.value_at(mat_5x4_int, (5,5))
    assert None == m.value_at(mat_5x4_int, (5,4))
    assert None == m.value_at(mat_5x4_int, (-1,1))
