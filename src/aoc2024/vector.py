
def sub(u: list[int], v: list[int]) -> list[int]:
    """Subtract two lists elementwise"""
    len_u, len_v = len(u), len(v)
    if len_u != len_v:
        raise ValueError(
            f"Vectors must of the the same length but got {len_u} and {len_v}"
        )
    res = [
        u[i] - v[i]
        for i in range(len_u)
    ]
    return type(u)(res)


def add(u: list[int], v: list[int]) -> list[int]:
    """Add two lists elementwise"""
    len_u, len_v = len(u), len(v)
    if len_u != len_v:
        raise ValueError(
            f"Vectors must of the the same length but got {len_u} and {len_v}"
        )
    res = [
        u[i] + v[i]
        for i in range(len_u)
    ]
    return type(u)(res)
