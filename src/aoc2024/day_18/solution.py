#!/usr/bin/env python

from typing import Optional
import math

from aoc2024 import load_input, from_env, to_numbers, matrix as m, vector as vct


DEBUG = from_env()

def measure_distance(grid, start: tuple, end: tuple) -> Optional[int]:
    end = tuple(end)

    if DEBUG:
        print(f"From {start} --> {end}")

    queue = [start]
    while queue:
        xy = queue.pop(0)
        dist = m.value_at(grid, xy)

        if tuple(xy) == end:
            return dist

        for nxy, ndist in m.around(grid, xy):
            if ndist == 0:
                m.set_value_at(grid, nxy, dist + 1)
                queue.append(nxy)


def solve_p1(fpath = None, shape = [71, 71], n_steps=1024, quiet=False):
    positions = load_input(fpath, line_parser=to_numbers)

    grid = m.create(*shape, 0)
    for t in range(n_steps):
        m.set_value_at(grid, positions[t], -1)

    if DEBUG:
        m.print(grid, header = "--- Initial grid ---")

    res = measure_distance(grid, (0, 0), vct.add(shape, (-1, -1)))

    if DEBUG:
        m.print(grid, header = "--- Final grid ---")

    if not quiet:
        print(res)

    return res


def solve_p2(fpath = None, shape = [71, 71]):
    """
    To find the position, we traverse the list of them as in binary search
    and check if this is a solution by simply running solve_p1.

    Runtime (user)
    --------------
    python: 0.09
    pypy: 0.09
    """
    positions = load_input(fpath)
    solutions = []

    # binary search
    l, r = 0, len(positions)
    for _ in range(int(math.log2(r)) + 1):
        n = (l+r) // 2
        dist = solve_p1(fpath, shape, n+1, quiet=True)
        if dist is None:
            solutions.append(n)
            r = n
        else:
            l = n

    n = solutions.pop()
    res = positions[n]
    print(res)

    return res


def solve_p2_v1(fpath = None, shape = [71, 71]):
    """
    Brute force solution that simply delegates to solve_p1: for every
    position in the list, the whole process (solve_p1) is repeated from
    the very beginning.

    Runtime (user)
    --------------
    python: 46,80
    pypy: 12,95
    """
    positions = load_input(fpath, line_parser=to_numbers)

    xy = (-1, -1)
    for n, pos in enumerate(positions):
        if solve_p1(fpath, shape, n+1, quiet=True) is None:
            xy = pos
            break

    res = ",".join(map(str, xy))
    print(res)

    return res


if __name__ == "__main__":
    solve_p1("test.1.txt", [7, 7], 12) #=> 22
    solve_p1() #=> 246

    solve_p2("test.1.txt", [7, 7]) #=> 6,1
    solve_p2() #=> 22,50
