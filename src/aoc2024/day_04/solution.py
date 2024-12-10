#!/usr/bin/env python

from itertools import product
from typing import Any

from aoc2024 import load_input
from aoc2024 import matrix as m


DIRECTIONS = [
    (0, 1), (0, -1),  # horizontal
    (1, 0), (-1, 0),  # vertical
    (1, 1), (-1, -1), # main diagonal
    (-1,1), (1, -1),  # minor diagonal
]


def has_word_at(word, matrix, xy, dxy) -> bool:
    if not word:
        return True

    if m.value_at(matrix, xy) != word[0]:
        return False

    nxy = tuple([xy[i] + dxy[i] for i in range(len(xy))])

    return has_word_at(word[1:], matrix, nxy, dxy)


def solve_p1(fpath = None):
    brd = load_input(fpath)

    count = 0
    maxx, maxy = m.shape(brd)

    for xy in product(range(maxx), range(maxy)):
        count += sum(
            has_word_at("XMAS", brd, xy, dxy)
            for dxy in DIRECTIONS
        )

    print(count)

    return count


def solve_p2(fpath = None):
    brd = load_input(fpath)

    # start at top left and top right corners of X
    maxx, maxy = m.shape(brd)
    count = 0
    for tl in product(range(maxx-2), range(maxy-2)):
        tr = (tl[0], tl[1] + 2)
        # print( (tl, m.value_at(brd, tl)), (tr, m.value_at(brd, tr)))

        # check along main diagonal downwards
        major = (
            has_word_at("MAS", brd, tl, (1,1))
            or
            has_word_at("SAM", brd, tl, (1,1))
        )

        # check along minor diagonal downwards
        minor = (
            has_word_at("MAS", brd, tr, (1,-1))
            or
            has_word_at("SAM", brd, tr, (1,-1))
        )

        # print(major, minor)

        if major and minor:
            # print("..Found")
            count += 1

    print(count)

    return count


if __name__ == "__main__":
    solve_p1("test.1.txt") #=> 18
    solve_p1() #=> 2517

    solve_p2("test.1.txt") #=> 9
    solve_p2() #=> 1960
