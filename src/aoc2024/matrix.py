
def shape(matrix: list[list]) -> tuple[int, int]:
    return (len(matrix), len(matrix[0]))


def value_at(matrix: list[list], coord: tuple[int, int]):
    x, y = coord
    if 0 <= x < len(matrix) and 0 <= y < len(matrix[0]):
        return matrix[x][y]
    return None
