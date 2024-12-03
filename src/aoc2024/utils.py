"""
General purpose utilities for AOC2024
"""

from typing import Any, Callable


def load_input(
    fpath: str = None,
    *,
    line_parser: Callable = None,
) -> list[Any]:
    """
    Write something here :)

    Arguments
    ---------

    Keyword-only arguments
    ----------------------

    Returns
    -------

    """

    fpath = fpath or "input.txt"

    with open(fpath) as ifd:
        lines = list(map(str.strip, ifd.readlines()))

    if line_parser:
        lines = list(map(line_parser, lines))

    return lines


def to_numbers(line: str, cls=int) -> list[int]:
    """
    Split line by whitespace (one or many) to a list of integers.

    Arguments
    ---------
    line : str
        a single line of text
    cls : type, default = int
        convert each item to this type

    Returns
    -------
    A list of objects of type `cls`
    """

    return list(map(cls, line.split()))
