import itertools
from typing import Callable, Optional

from .utils import load_input
from .vector import add as vadd

# TODO:
# pprint() for pretty printing of the matrix

UP    = (-1,  0)
DOWN  = ( 1,  0)
LEFT  = ( 0, -1)
RIGHT = ( 0,  1)

# synonymous terminology: north, south, west, east, north-west, ...
N = UP
S = DOWN
W = LEFT
E = RIGHT

NW = (-1, -1)
NE = (-1,  1)
SW = ( 1, -1)
SE = ( 1,  1)

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
    """

    TODO:
    allow passing a predicate to filter by position and/or value
    This will work like `findall()`
    """
    maxx, maxy = shape(matrix)
    for x, y in itertools.product(range(maxx), range(maxy)):
        if with_value:
            yield (x, y), matrix[x][y]
        else:
            yield (x, y)


def find(matrix: list[list], value) -> Optional[tuple]:
    """ find the first occurrence of `value` in the matrix

    Arguments
    ---------
    matrix :
    value :
        a value or a callable/predicate to test value against

    Returns
    -------
    None if nothing was found
    Otherwise, a tuple of two values, the first being a coordinate xy
    and the second the value at that coordinate

    """
    if callable(value):
        is_ok = lambda x: value(x)
    else:
        is_ok = lambda x: value == x

    for xy, v in scan(matrix, with_value=True):
        if is_ok(v):
            return xy, v


def around(matrix: list[list], xy: tuple[int, int]):
    """
    Yield cells that are around given cell `xy` with the values.
    Around means four points located along the horizontal and vertical axes.

    Yields
    ------
    Tiple[(x, y), value] :
        the cell coordinate and the cell value

    TODO:
    allow more complex directions? e.g. diagonal, via parameter? (e.g. day_14)
    """
    directions = [UP, DOWN, LEFT, RIGHT]
    maxx, maxy = shape(matrix)
    for dxy in directions:
        x, y = vadd(xy, dxy)
        if 0 <= x < maxx and 0 <= y < maxy:
            yield type(xy)([x, y]), matrix[x][y]


original_print = print

def print(
    matrix: list[list],
    *,
    header: str = None,
    footer: str = None,
    row_hook: Callable = None,
):
    """ Print 2D matrix """
    if header:
        original_print(header)
    for row in matrix:
        if row_hook is not None:
            row = row_hook(row)
        original_print(row)
    if footer:
        original_print(footer)


def create(height: int, width: int, value = None) -> list[list]:
    """
    Create a 2D matrix of shape (height, width) and fill it with values `value`

    Arguments
    ---------
    height : int
    width : int
    value : optional

    Returns
    -------
    list of lists of values (2D matrix of values)
    """
    mat = [
        [value] * width
        for _ in range(height)
    ]
    return mat