#!/usr/bin/env python

# # #
# TODO
# 1) use networkx, build a DAG and check for connectivity

from aoc2024 import from_env
from aoc2024 import matrix as m

DEBUG = from_env()


def count_reachable_ends(area, start, ends) -> int:
    """
    Trailhead score is the number of ends that can be reached from given start.
    """

    def collect_reachable_ends(start, reached):
        if start in ends:
            reached.add(start)
        else:
            height = m.value_at(area, start)
            for xy, v in m.around(area, start):
                if v == height + 1:
                    collect_reachable_ends(xy, reached)

    reached = set()
    collect_reachable_ends(start, reached)

    return len(reached)


def count_reachable_ends_v1(area, start, ends) -> int:
    """
    Trailhead score is the number of ends that can be reached from given start.

    This implementation is slow because its tests every pair of (start, end)
    separately.
    """

    def is_reachable(start, end) -> bool:
        if start == end:
            return True

        height = m.value_at(area, start)
        for xy, v in m.around(area, start):
            if v == height + 1 and is_reachable(xy, end):
                return True

        return False

    return sum(
        is_reachable(start, end)
        for end in ends
    )


def count_hiking_trails(area, start, ends) -> int:
    """
    Count the number of paths between `start` and any of `ends`
    """
    if start in ends:
        return 1

    height = m.value_at(area, start)
    return sum(
        count_hiking_trails(area, xy, ends)
        for xy, v in m.around(area, start)
        if v == height + 1
    )


def load(fpath = None):
    starts, ends = [], []

    def collect_trailhead_ends(xy, v):
        if v == 0:
            starts.append(xy)
        if v == 9:
            ends.append(xy)

    area = m.load(fpath, as_type=int, hook=collect_trailhead_ends)

    return area, starts, ends


def solve(fpath, scorer):
    area, starts, ends = load(fpath)
    score = sum(
        scorer(area, start, ends)
        for start in starts
    )
    print(score)
    return score


def solve_p1_v1(fpath = None):
    return solve(fpath, count_reachable_ends_v1)


def solve_p1(fpath = None):
    return solve(fpath, count_reachable_ends)


def solve_p2(fpath = None):
    return solve(fpath, count_hiking_trails)


if __name__ == "__main__":
    solve_p1("test.1.txt") #=> 36
    solve_p1() #=> 794

    solve_p2("test.1.txt") #=> 81
    solve_p2() #=> 1706
