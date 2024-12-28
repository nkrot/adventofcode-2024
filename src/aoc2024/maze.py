# used in days: 06, 16, 20

from aoc2024 import matrix as mat

WALL = "#"

def load(source=None, pois=None, verbose=False):
    """
    Load the maze from the file `source` and 2D matrix.
    Additionally, find "points of interest" (pois) that are  tiles in the maze
    marked with a specific character. For example, S for start and E for end.

    Arguments
    ---------
    source : str
        path to the file
    pois : an iterable, optional
        "points of interest", a list of characters to look for.
    verbose : bool, default is True

    Returns
    -------
    a 2D matrix (maze)
    optionally, points of interest, as many as items in poi

    TODO:
    2) a poi can have multiple instances, then return a list of them
    3) src can be a path to file or a list[list[str]]
    """

    _pois = {}
    def _find_pois(xy, v):
        if v in pois:
            _pois[v] = xy

    kwargs = {}
    if pois is not None:
        kwargs["hook"] = _find_pois

    maze = mat.load(source, **kwargs)

    if verbose:
        mat.print(maze)
        for ch in pois:
            print(ch, _pois[ch])

    if pois is None:
        return maze
    else:
        extras = [_pois.get(ch, None) for ch in pois]
        return maze, *extras
