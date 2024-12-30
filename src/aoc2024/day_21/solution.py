#!/usr/bin/env python

# # #
# this implementation is very slow
#

from aoc2024 import load_input, from_env
from aoc2024.day_21 import directional_keypad as dkp, numeric_keypad as nkp

DEBUG = from_env()


def compute_code_complexity(code: str, seq: str | int) -> int:
    num = int(code[:-1])
    length = len(seq) if isinstance(seq, str) else seq
    return num * length


def type_code(code):
    for dircode_1 in nkp.type_code(code, "A"):
        for dircode_2 in dkp.type_code(dircode_1, "A"):
            for dircode_3 in dkp.type_code(dircode_2, "A"):
                yield dircode_3


def solve_p1(fpath = None):
    """
    Runtime (user time) | real input | test.1.txt
    --------------------|------------|------------
    python 3.10         |  505,21    | 78,11
    pypy 3.10           |  211,15    | 34,11
    """
    codes = load_input(fpath)

    min_length_codes = {}
    for code in codes:
        min_length_codes[code] = (10000, )
        for seq in type_code(code):
            if len(seq) < min_length_codes[code][0]:
                min_length_codes[code] = (len(seq), seq)
                # print(code, len(seq), seq)
        print(code, min_length_codes[code])

    res = sum(
        compute_code_complexity(code, length[0])
        for code, length in min_length_codes.items()
    )

    print(res)

    return res


def solve_p2(fpath = None):
    x = load_input(fpath)
    res = 1
    print(res)

    return res


if __name__ == "__main__":
    solve_p1("test.1.txt") #=> 126384
    solve_p1() #=> 206798

    #solve_p2("test.1.txt") #=>
    #solve_p2() #=>
