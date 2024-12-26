#!/usr/bin/env python

# # #
# numpy provides necessary functionality too but it too heavy as a dependency
#

from functools import reduce

from aoc2024 import load_input, from_env, vector as vct

DEBUG = from_env()


def load(fpath):
    def _parse(line):
        return [int(ch == "#") for ch in line]

    blocks = load_input(fpath, by_blocks=True, line_parser=_parse)

    lock_or_key = {0: [], 5: []}
    for blk in blocks:
        lock_or_key[sum(blk[0])].append(blk)

    return lock_or_key[5], lock_or_key[0]  # locks, keys


def count_pin_heights(mat: list[list[int]]):
    return reduce(
        lambda colsum, v: vct.add(colsum, v),
        mat,
        [-1] * len(mat[0])
    )


def do_overlap(lock, key) -> bool:
    """Check if the lock and the key overlap in terms of pin heights"""
    return any(h >= 6 for h in vct.add(lock, key))


def solve_p1(fpath = None):
    locks, keys = load(fpath)

    lock_pins = [count_pin_heights(lock) for lock in locks]
    key_pins = [count_pin_heights(key) for key in keys]

    res = sum(
        not(do_overlap(lock, key))
        for lock in lock_pins
        for key in key_pins
    )
    print(res)

    return res


def solve_p2(fpath = None):
    res = 0
    print(res)

    return res


if __name__ == "__main__":
    solve_p1("test.1.txt") #=> 3
    solve_p1() #=> 3287

    # solve_p2("test.1.txt") #=>
    # solve_p2() #=>
