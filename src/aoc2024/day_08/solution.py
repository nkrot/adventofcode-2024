#!/usr/bin/env python

import itertools
from collections import defaultdict
from typing import Callable

from aoc2024 import load_input, from_env
from aoc2024 import matrix as m
from aoc2024 import vector as vct

DEBUG = from_env()


def solve(fpath: str, get_antinode: Callable) -> int:
    """
    Common part of both tasks:
    1) load the task inputs
    2) extract antennas grouping them by frequency (letter/digit)
    3) for each valid pair of antennas (of the same frequency), collect
       all antinodes for that pair using provided function `get_antinode()`
    4) ensure that resulting list of antinodes does not have duplicates
    5) return the number of antinodes
    """
    city = load_input(fpath, line_parser=list)
    # print(city)

    antennas = defaultdict(list)
    for xy,v in m.scan(city, with_value=True):
        if v != ".":
            antennas[v].append(xy)

    if DEBUG:
        print(antennas)

    antinodes = set()
    for anns in antennas.values():
        for a, b in itertools.combinations(anns, 2):
            antinodes.update(list(get_antinode(city, a, b)))

    return len(antinodes)


def solve_p1(fpath = None):

    def antinodes(city, a, b):
        dist = vct.sub(a, b)
        for nd in [vct.add(a, dist), vct.sub(b, dist)]:
            if m.value_at(city, nd):
                yield nd

    res = solve(fpath, antinodes)
    print(res)

    return res


def solve_p2(fpath = None):

    def antinodes(city, a, b):
        yield a
        yield b

        dist = vct.sub(a, b)

        for curr, op in [(a, vct.add), (b, vct.sub)]:
            while True:
                curr = op(curr, dist)
                if m.value_at(city, curr):
                    yield curr
                else:
                    break

    res = solve(fpath, antinodes)
    print(res)

    return res


if __name__ == "__main__":
    solve_p1("test.1.txt") #=> 14
    solve_p1() #=> 271

    solve_p2("test.1.txt") #=> 34
    solve_p2() #=> 994
