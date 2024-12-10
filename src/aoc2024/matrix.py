import itertools
from typing import Callable

from .utils import load_input
from .vector import add as vadd

# TODO:
# pprint() for pretty printing of the matrix

UP = (-1, 0)
DOWN = (1, 0)
LEFT = (0, -1)
RIGHT = (0, 1)


def load(
    fpath: str = None,
    as_type: Callable = None,
    hook: Callable = None,  # TODO: rename
    #collect: Callable = None,
):
    """
    Load matrix from the file `fpath`

    Arguments
    ---------
    fpath: str
        path to the file to load
    as_type : Callable, optional
        convert all values to type
    hook : Callable, optional
        a callback that will be envoked for each cell in the matrix
        yielding ((x,y), value). Here the value is after applying `as_type`

    Returns
    -------
    list[list[Any]] :
        2D matrix
    """

    m = load_input(fpath, line_parser=list)

    if as_type is not None:
        for (x, y), v in scan(m, with_value=True):
            m[x][y] = as_type(v)

    if hook is not None:
        for (x, y), v in scan(m, with_value=True):
            hook((x,y), v)

    return m


def shape(matrix: list[list]) -> tuple[int, int]:
    return (len(matrix), len(matrix[0]))


def value_at(matrix: list[list], coord: tuple[int, int]):
    x, y = coord
    if 0 <= x < len(matrix) and 0 <= y < len(matrix[0]):
        return matrix[x][y]
    return None


def set_value_at(matrix: list[list], coord: tuple[int, int], value):
    oldval = None
    x, y = coord
    if 0 <= x < len(matrix) and 0 <= y < len(matrix[0]):
        oldval = matrix[x][y]
        matrix[x][y] = value
    return oldval


def scan(matrix: list[list], with_value: bool=False):
    maxx, maxy = shape(matrix)
    for x, y in itertools.product(range(maxx), range(maxy)):
        if with_value:
            yield (x, y), matrix[x][y]
        else:
            yield (x, y)


def around(matrix: list[list], xy: tuple[int, int]):
    """
    Yield cells that are around given cell `xy` with the values.
    Around means four points located along the horizontal and vertical axes.

    Yields
    ------
    Tiple[(x, y), value] :
        the cell coordinate and the cell value

    TODO:
    allow more complex directions? e.g. diagonal, via parameter?
    """
    directions = [UP, DOWN, LEFT, RIGHT]
    maxx, maxy = shape(matrix)
    for dxy in directions:
        x, y = vadd(xy, dxy)
        if 0 <= x < maxx and 0 <= y < maxy:
            yield type(xy)([x, y]), matrix[x][y]
