#!/usr/bin/env python

# # #
# solve_p1:
# initial: when patterns is a list
# real 2,11   user 2,09
# with frozendict
# real 0,44   user 0,43
#
# solve_p2
# initially: when patterns is a list
# real 5,69   user 5,68
# when patterns is a frozendict
# real 1,29   user 1,28
# using sum+map+_count instead of a simple loop makes it slower
# real 2,19   user 2,17

import frozendict
import functools

from aoc2024 import load_input, from_env

DEBUG = from_env()

def load(fpath):
    """
    we group pattern by the first letter. When we iterate over the patterns
    later, we will need iterate over the relevant subset of them only.
    {
      'r': ('r', 'rb'),
      'w': ('wr',),
      'b': ('b', 'br', 'bwu'),
      'g': ('g', 'gb')
    }
    """

    pattern, designs = load_input(fpath, by_blocks=True)

    patterns = pattern[0].replace(',', '').split()
    # patterns.sort()

    # initial implementation
    #return tuple(patterns), designs

    patterns = functools.reduce(
        lambda d, pat: (d.setdefault(pat[0], []).append(pat), d)[1],
        patterns,
        {},
    )

    # convert RHS of the dict to tuple to make them hashable
    for pat in patterns:
        patterns[pat] = tuple(sorted(patterns[pat]))

    # print(patterns)
    # print(designs)

    return frozendict.frozendict(patterns), designs


@functools.lru_cache()
def is_possible(design, patterns, lvl=0) -> bool:
    if DEBUG:
        print(f"{'.'*lvl}design: {design}")

    def _check(pat):
        if DEBUG:
            print(f"_check: {pat}")
        return (
            design.startswith(pat)
            and
            is_possible(design[len(pat):], patterns, lvl+1)
        )

    if not design:
        return True

    return any(map(_check, patterns.get(design[0], [])))


@functools.lru_cache()
def count_possible(design, patterns, lvl=0) -> int:
    # print(f"{'.'*lvl}design: {design}")

    def _count(pat):
        if DEBUG:
            print(f"_check: {pat}")
        if design.startswith(pat):
            return count_possible(design[len(pat):], patterns, lvl+1)
        return 0

    if not design:
        return 1

    return sum(map(_count, patterns.get(design[0], [])))

    # This implementation is faster
#     cnt = 0
#     for pat in patterns.get(design[0], []):
#         if design.startswith(pat):
#             cnt += count_possible(design[len(pat):], patterns, lvl+1)
#
#     return cnt


def solve(fpath, func):
    patterns, designs = load(fpath)
    res = sum(
        func(design, patterns)
        for design in designs
    )
    print(res)
    return res


def solve_p1(fpath = None):
    return solve(fpath, is_possible)


def solve_p2(fpath = None):
    return solve(fpath, count_possible)


if __name__ == "__main__":
    solve_p1("test.1.txt") #=> 6
    solve_p1() #=> 317

    solve_p2("test.1.txt") #=> 16
    solve_p2() #=> 883443544805484
