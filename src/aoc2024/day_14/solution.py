#!/usr/bin/env python

from collections import defaultdict
from functools import reduce

from aoc2024 import load_input, from_env, to_numbers
from aoc2024 import matrix as m, vector as vkt

DEBUG = from_env()

def load(fpath):
    robots = [
        ((x, y), (dx, dy))
        for x,y,dx,dy in load_input(fpath, line_parser=to_numbers)
    ]
    return robots


def move_robot(robot, t, space):
    """move robot in space t times """

    (x, y), (dx, dy) = robot

    x = (x + dx*t) % space[0]
    y = (y + dy*t) % space[1]

    return ((x, y), (dx, dy))


def count_by_quadrants(robots, space) -> dict:
    # middle lines that split the space in 4 quadrants
    midx, midy = space[0] // 2, space[1] // 2

    # allocate each robot to a quadrant and count
    quadrants = defaultdict(int)
    for rbt in robots:
        (x, y), _ = rbt
        if x == midx or y == midy:
            continue
        qdrt = (x < midx, y < midy)
        quadrants[qdrt] += 1

    return quadrants


def has_xmas_tree(robots, space) -> bool:
    """
    we detect presence of a Xmas tree by finding a cluster of robots that
    form a 3x3 square:
        ###
        ###
        ###
    in the hope that it will be sufficient.
    """
    dirs = [m.N, m.S, m.W, m.E, m.NW, m.NE, m.SW, m.SE]
    maxx, maxy = space

    # the matrix for holding counts of how many neighbors a position xy has
    counts = [
        [0] * maxy
        for _ in range(maxx)
    ]

    visited = set()
    for xy, _ in robots:
        # if is sufficient to investigate a single robot from a location.
        # considering more robots will lead to overcounts.
        if xy in visited:
            continue
        visited.add(xy)

        # mark all positions to which a robot contributes, including itw own
        x, y = xy
        counts[x][y] += 1

        for dxy in dirs:
            nx, ny = vkt.add(xy, dxy)
            if 0 <= nx < maxx and 0 <= ny < maxy:
                counts[nx][ny] += 1

    # find the position with max number of neightbors
    maxval = 0
    for row in counts:
        maxval = max(maxval, max(row))

    ok = maxval > len(dirs)
    # if ok:
    #     print(maxval)

    return ok


def solve_p1(fpath = None, space=[101, 103]):
    robots = load(fpath)
    t = 100

    robots = [
        move_robot(rbt, t, space)
        for rbt in robots
    ]

    quadrants = count_by_quadrants(robots, space)

    res = reduce(lambda p, v: p*v, quadrants.values(), 1)
    print(res)

    return res


def solve_p2(fpath = None, space=[101, 103]):
    """
    Runtime for real input
    python: 19,14
    pypy:    2,04

    """
    robots = load(fpath)

    # The arrangements of robots repeat over time.
    # someone on the forum said x repeat every space[0] and
    # y repeats every space[1] times
    # for t in range(space[0]*space[1]):
    #     robots = [
    #         move_robot(rbt, 1, space)
    #         for rbt in robots
    #     ]
    #     if has_xmas_tree(robots, space):
    #         draw(robots, space, 1+t)

    t = 0
    while t <= space[0]*space[1]:
        t += 1
        robots = [
            move_robot(rbt, 1, space)
            for rbt in robots
        ]
        if has_xmas_tree(robots, space):
            draw(robots, space, t)
            break

    print(t)

    return t


def draw(robots, space, t):
    print(f"--- Timestamp {t} ---\n")
    row = "." * space[0]
    canvas = [
        list(row)
        for _ in range(space[1])
    ]

    for rbt in robots:
        x, y = rbt[0]
        canvas[y][x] = "#"

    print("\n".join(map("".join, canvas)))
    print("")


if __name__ == "__main__":
    solve_p1("test.1.txt", [11, 7]) #=>
    solve_p1() #=> 208437768

    solve_p2("test.1.txt", [11, 7]) #=>
    solve_p2() #=> 7492
