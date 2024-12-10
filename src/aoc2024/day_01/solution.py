#!/usr/bin/env python

from collections import Counter

from aoc2024 import utils


def load(path):
    pairs = utils.load_input(path, line_parser=utils.to_numbers)

    lists = [
        [pair[0] for pair in pairs],
        [pair[1] for pair in pairs]
    ]

    return lists


def solve_p1(path):
    ls, rs = load(path)
    ls.sort()
    rs.sort()

    assert len(ls) == len(rs)

    diffs = [abs(a-b) for a, b in zip(ls, rs)]

    res = sum(diffs)
    print(res)

    return res


def solve_p2(path):
    ls, rs = load(path)

    counts_ls = Counter(ls)
    counts_rs = Counter(rs)

    scores = [
        lnum * counts_rs[lnum] * lcnt
        for lnum, lcnt in counts_ls.items()
    ]

    res = sum(scores)
    print(res)

    return res



if __name__ == "__main__":

    solve_p1("test.1.txt")  # = 11
    solve_p1("input.txt") #=> 1197984

    solve_p2("test.1.txt")  # => 31
    solve_p2("input.txt")  #=> 23387399
