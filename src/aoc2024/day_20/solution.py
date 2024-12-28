#!/usr/bin/env python

from collections import defaultdict

from aoc2024 import (
   load_input, from_env, matrix as mat, maze as mz, vector as vct
)

DEBUG = from_env()

def walk(maze, start, end):
    """in bfs fashion

    For abstracting
    1) allow or not visiting previously visited tiles?
    """
    mat.set_value_at(maze, start, 0)

    # depending on bfs/dfs, use stack or queue
    # how to allow more complex cases like PriorityQueue?
    tiles = [start]

    while tiles:
        curr = tiles.pop(0)
        dist = mat.value_at(maze, curr)
        for xy, val in mat.around(maze, curr):
            # if val == mz.WALL:
            #     continue
            if val in {".", "E"}:
                mat.set_value_at(maze, xy, 1+dist)
                tiles.append(xy)

    # TODO: how to move rjust_cells to mat.print()?
    def rjust_cells(cells, width=2):
        # assumung the widest value in a cell is of length 2
        return [str(cell).rjust(width) for cell in cells]

    if DEBUG:
        mat.print(maze, row_hook=rjust_cells)

def are_all_tracks_visited(maze) -> bool:
    """
    """
    res = mat.find(maze, ".")
    if res:
        print(f"Unwalked track (.) found: {res}")
    else:
        print("All tracks (.) have been walked")

    return bool(res)


def cheat(maze):
    """
    """
    neighbors = [
        (mat.LEFT, mat.RIGHT),
        (mat.UP,   mat.DOWN),
    ]
    counts = defaultdict(int)
    for wall, _ in mat.findall(maze, "#"):
        for offsets in neighbors:
            a, b = [
                mat.value_at(maze, vct.add(wall, off))
                for off in offsets
            ]
            if isinstance(a, int) and isinstance(b, int):
                saved = abs(a-b) - 2
                counts[saved] += 1

    return counts


def solve_p1(fpath = None, cutoff = 100):
    maze, start, end = mz.load(fpath, "SE")

    walk(maze, start, end)
    # print("Distance", mat.value_at(maze, end))

    assert not are_all_tracks_visited(maze), "Algorithm does not apply"

    counts = cheat(maze)
    # print(sorted(counts.items()))

    # How many cheats would save you at least 100 picoseconds?
    res = sum(
        cnt
        for saved, cnt in counts.items()
        if saved >= cutoff
    )
    print(res)

    return res

# 84 - 18 + 2 = 64

def solve_p2(fpath = None):
    x = load_input(fpath)
    res = 1
    print(res)

    return res


if __name__ == "__main__":
    solve_p1("test.1.txt", 30) #=>
    solve_p1() #=> 1332

    #solve_p2("test.1.txt") #=>
    #solve_p2() #=>
