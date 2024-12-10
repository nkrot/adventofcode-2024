#!/usr/bin/env python

import re

from aoc2024 import load_input


def solve_p1(fpath = None):
    lines = load_input(fpath)
    res = 0
    for line in lines:
        for m in re.finditer(r'mul\((\d+),(\d+)\)', line):
            res += int(m[1]) * int(m[2])
    print(res)

    return res


def solve_p2(fpath = None):
    lines = load_input(fpath)
    res = 0
    doit = True
    for line in lines:
        for m in re.finditer(r'mul\((\d+),(\d+)\)|do(n\'t)?\(\)', line):
            if m[0].startswith("don\'t"):
                doit = False
            elif m[0].startswith("do"):
                doit = True
            elif doit:
                res += int(m[1]) * int(m[2])
    print(res)

    return res


if __name__ == "__main__":
    solve_p1("test.1.txt") #=> 161
    solve_p1() #=> 175615763
    solve_p2("test.2.txt")  #=> 48
    solve_p2() #=> 74361272

