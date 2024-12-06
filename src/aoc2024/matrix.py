import itertools

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
