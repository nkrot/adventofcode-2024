from dataclasses import dataclass
from importlib import resources


@dataclass
class TData:
    """
    Container for test input and expected outcomes of both parts of the task.

    Example
    -------
    from tests.aoc2024.helpers import TData
    from aoc2024 import day_07
    from aoc2024.day_07.solution import solve_p1, solve_p2

    td = TData(day_07, "test.1.txt", 10, 100)
    assert td.expected_p1 == solve_p1(td.path)
    assert td.expected_p2 == solve_p2(td.path)
    """
    path: str
    expected_p1: str | int
    expected_p2: str | int

    @classmethod
    def from_module(cls, mdl, fname, exp1, exp2):
        path = resources.path(mdl, fname)
        # TODO: check that `path` is valid file
        return cls(path, exp1, exp2)


# def make_tdata(*args):
#     return TData(*args)

# def make_tdata2(mdl, fname, exp1, exp2):
#     return TData(
#         resources.path(mdl, "test.1.txt"),
#         exp1,
#         exp2
#     )
