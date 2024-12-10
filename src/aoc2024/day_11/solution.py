#!/usr/bin/env python

# # #
# without caching the function, solve_p2 would run very long...
#

from functools import lru_cache
from aoc2024 import load_input, from_env, to_numbers

DEBUG = from_env()


def evolve(stone, msg=""):
    s = str(stone)
    if stone == 0:
        res = (1,)
    elif len(s) % 2 == 0:
        i = len(s) // 2
        res = (int(s[:i]), int(s[i:]))
    else:
        res = (stone * 2024,)
    if DEBUG:
        print(f"{msg}{stone} --> {res}")
    return res


@lru_cache(maxsize=None)
def blink(stones, times):
    if times == 0:
        return len(stones)

    return sum(
        blink(evolve(stone, f"{'.' * times}at {times}: "), times-1)
        for stone in stones
    )


def solve_p1(fpath = None, times = 25):
    stones = load_input(fpath, line_parser=to_numbers)[0]
    res = blink(tuple(stones), times)
    print(res)
    return res


def solve_p2(fpath = None):
    return solve_p1(fpath, 75)


if __name__ == "__main__":
    solve_p1("test.1.txt") #=> 55312
    solve_p1() #=> 202019

    solve_p2("test.1.txt") #=> 65601038650482
    solve_p2() #=> 239321955280205
