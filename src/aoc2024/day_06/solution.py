#!/usr/bin/env python

from copy import deepcopy

from aoc2024 import from_env
from aoc2024 import matrix as m, maze as mz, vector as vct

DEBUG = from_env()
TURNS = (m.UP, m.RIGHT, m.DOWN, m.LEFT)


def load(fpath = None):
    maze, guard = mz.load(fpath, "^")
    guard = [guard, m.UP, 1]

    for (x,y), v in m.scan(maze, with_value=True):
        if v != "#":
            maze[x][y] = 0

    x, y = guard[0]
    maze[x][y] = 1

    if DEBUG:
        print(maze)
        print(guard)

    return maze, guard


def print_maze(maze):
    """In a more user-friendly form"""
    def _row2str(row):
        cells = [
            ("." if v == 0 else str(v)).rjust(2)
            for v in row
        ]
        return " ".join(cells)

    m.print(maze, row_hook=_row2str)


def turn(guard):
    """Turn the guard to the right in place"""
    curr = TURNS.index(guard[1])
    nxt = (1 + curr) % len(TURNS)
    guard[1] = TURNS[nxt]


def test_turn():
    guard = [(0, 0), m.UP]
    print(guard)
    for _ in range(5):
        turn(guard)
        print(guard)

# test_turn()
# exit(100)

def move(maze, guard):
    """
    The guard takes one step.

    Both maze and guard are modified in place!
    """
    # new (target) position
    xy = vct.add(guard[0], guard[1])

    v = m.value_at(maze, xy)

    # future position is off the maze. cannot move
    if v is None:
        return False

    if v in {"#", "O"}:  # hit the obstacle
        turn(guard)
        return move(maze, guard)

    else:  # free to move to the new position
        guard[0] = xy
        if v == 0:  # first time visiting this cell
            guard[2] += 1
            m.set_value_at(maze, guard[0], guard[2])
        return True

#def walk(maze, guard):
#   """ it doesnot make sense because guard is modified anyway"""
#    n = 0
#    while move(maze, guard):
#        n += 1
#        yield n, guard


def solve_p1(fpath = None):
    maze, guard = load(fpath)
    while move(maze, guard): pass
    if DEBUG:
        print_maze(maze)
        print(guard)
    print(guard[2])
    return guard[2]


# p2: Optimizations
# 1) Now that we collect the path, there is no need to modify the maze.
# This means, we dont need to make a copy of it.

def solve_p2(fpath = None):
    return solve_p2_v2(fpath)


def solve_p2_v3(fpath = None):
    """
    We dont need to run simulation from the very beginning each time.
    Start just before newly added obstacle.
    """

    # Algorithm
    # compute original path
    # for each position in the path, put an O just on front of it
    # and run simulation from that position.
    # When putting an obstacle, be careful with # as we need to place it
    # at the position that is in front of the guard *after* he turns
    pass

def position_in_front_of(guard, maze):
    """
    Compute position of the obstacle to put in front of the guard.
    If the position in front is already occupied by #, try next position
    that is turned to the right wrt the guard
    """
    # we want to check all directions starting with the current one
    # and then going clockwise
    i = TURNS.index(guard[1])
    for di in range(len(TURNS)):
        j = (i + di) % len(TURNS)
        dxy = TURNS[j]

        xy = vct.add(guard[0], dxy)
        if m.value_at(maze, xy) != "#":
            return xy


def solve_p2_v2(fpath = None):
    """
    Optimized version of solve_p2_v1
    Instead of trying to put an obstacle at any position, we try only
    the positions along the route the guard walks.

    Runtime: (DEBUG=1)
    -------
    python3.10: user  834,77
    pypy3.10  : user 1114,82
    """
    maze, guard = load(fpath)

    obstacles = set()
    obstacles.add(position_in_front_of(guard, maze))

    _maze = deepcopy(maze)
    _guard = deepcopy(guard)
    while move(_maze, _guard):
        obstacles.add(position_in_front_of(_guard, maze))

    obstacles = sorted(obstacles)

    if DEBUG:
        print_maze(_maze)
        print("CANDIDATE OBSTACLES", obstacles)

    c = 0
    for xy in obstacles:
        v = m.value_at(maze, xy)
        if DEBUG:
            print("Checking", xy, v)
        if v == 0 and has_loop(maze, guard, xy):
            c += 1
    print(c)
    return c


def has_loop(maze, guard, xy) -> bool:
    """
    Add an obstacle at position xy and test if resulting maze has a loop
    """
    _guard = deepcopy(guard)
    _maze = deepcopy(maze)
    m.set_value_at(_maze, xy, "O")

    path = [guard]
    while move(_maze, _guard):
        if _guard in path:
            if DEBUG:
                print("PATH", path)
                print(_guard)
                print_maze(_maze)
            return True
        path.append(deepcopy(_guard))
    return False


def solve_p2_v1(fpath = None):
    """
    Runtime
    -------
    python3.10 : real 4111,01 ; user 4096,76
    pypy3.10   : real 5026,59 ; user 5005,80
    """
    maze, guard = load(fpath)

    cnt = 0
    for xy, v in m.scan(maze, with_value=True):
        if DEBUG:
            print("Checking", xy, v)
        if v == 0 and has_loop(maze, guard, xy):
            cnt += 1
    print(cnt)
    return cnt


if __name__ == "__main__":
    solve_p1("test.1.txt") #=> 41
    solve_p1() #=> 4722

    # solve_p2_v1("test.1.txt") #=> 6
    solve_p2("test.1.txt") #=> 6
    solve_p2() #=> 1602
