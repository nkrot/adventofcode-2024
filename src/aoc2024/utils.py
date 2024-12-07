"""
General purpose utilities for AOC2024
"""

import os
from typing import Any, Callable, Optional


def from_env(var: str = "DEBUG", alt = None) -> Optional[str|int]:
    """
    Get value of variable `var` from the environment. If `var` not
    provided, get value of the value DEBUG
    """
    val = os.environ.get(var, alt)
    if val and val.isdecimal():
        val = int(val)
    return val


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
