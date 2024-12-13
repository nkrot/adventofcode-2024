"""
General purpose utilities for AOC2024
"""

import os
import re
import functools
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
    fpath: str,
    *,
    by_blocks: bool = False,
    line_parser: Callable = None,
) -> list[Any]:
    """
    Write something here :)

    Arguments
    ---------
    fpath : str, optional, default = "input.txt"
        path to the file with input data

    Keyword-only arguments
    ----------------------
    by_blocks : bool, default = False
        treat empty lines in the file as separators between groups of lines
        and make lines into groups. This adds an outer list
    line_parser: Callable
        a function that will be envoked on every line. Useful for converting
        the line to something else, e.g. to a list of numbers

    Returns
    -------
    list[list[str]] :
        if by_blocks is True
    list[str] :
        if by_blocks is False
    """

    fpath = fpath or "input.txt"

    with open(fpath) as ifd:
        lines = list(map(str.strip, ifd.readlines()))

    if by_blocks:
        lines = group_lines(lines)

    if line_parser:
        if by_blocks:
            lines = [
                list(map(line_parser, lns))
                for lns in lines
            ]
        else:
            lines = list(map(line_parser, lines))

    return lines


def group_lines(lines: list[str]) -> list[list[str]]:
    """
    Make lines into groups of lines.
    An empty line is treated as a separator between groups.

    Arguments
    ---------
    lines: list of strings

    Returns
    -------
    list[list[str]] : a list of groups, where each group is a list of lines
    """
    def _group(lst, line):
        if len(line) == 0:
            lst.append([])
        else:
            lst[-1].append(line)
        return lst

    return functools.reduce(_group, lines, [[]])


def to_numbers(line: str, cls=int) -> list[int]:
    """
    Extract all numbers from given string `line`.
    The string is tokenized by any non-numerical character.

    Arguments
    ---------
    line : str
        a single line of text
    cls : type, default = int
        convert each item to this type

    Returns
    -------
    A list of objects of type `cls`

    Note
    ----
    Does not work for recognizing float numbers (that are point or comma
    separated).
    """

    return list(map(int, re.findall(r'\d+', line)))
