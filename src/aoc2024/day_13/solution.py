#!/usr/bin/env python

"""
Approach the task as a system of 2 linear equations.

    Button A: X+94, Y+34
    Button B: X+22, Y+67
    Prize: X=8400, Y=5400

is two linear equations:

    94*a + 22*b = 8400
    34*a + 67*b = 5400

where `a` and `b` is the number of times the button A and button B respectively
nedd to be pressed.

Only those solutions to the equation (a and b) are suitable as solutions
to the task that are integers.
"""

import numpy as np

from aoc2024 import load_input, from_env, to_numbers

DEBUG = from_env()


def load(fpath = None, task = 1):
    blocks = load_input(fpath, by_blocks=True, line_parser=to_numbers)

    if task == 2:
        addend = 10000000000000
        for lines in blocks:
            lines[-1] = [addend + v for v in lines[-1]]

    return blocks


def compute(m, costs=[3, 1]) -> int:
    """
    Button A: X+94, Y+34
    Button B: X+22, Y+67
    Prize: X=8400, Y=5400

    In this solution, values are named like this:
    a = [94, 34],
    b = [22, 67],
    c = [8400, 5400]
    """

    cost = 0
    a, b, c = m

    if DEBUG:
        print(m)
        print()
        print("a:", a)
        print("b:", b)
        print("c:", c)

    _y = (a[0] * c[1] - a[1] * c[0]) / (a[0] * b[1] - a[1]*b[0])
    _x = (c[0] - b[0] * _y) / a[0]

    if round(_x, 0) == _x and round(_y, 0) == _y:
        cost = costs[0] * _x + costs[1] * _y

    return int(cost)


def compute_with_numpy(m, costs=[3, 1]) -> int:
    """
    The solution uses numpy.linalg.solve()

    a = [
      [94, 34],
      [22, 67],
    ]
    c = [8400, 5400]
    """
    a = np.array(m[:2]).T
    c = np.array(m[2]).T

    if DEBUG:
        print(m)
        print()
        print("a:", a)
        print("c:", c)

    x = np.linalg.solve(a, c)
    if DEBUG:
        print("x:", x)
        print("Cx:", np.dot(a, x))

    # We need solutions only that are integer numbers.
    # To select such solutions, we transform x, plug them into
    # the equation and compare with values c. If both are equal,
    # the solution is accepted.

    # This approach is wrong, it truncates values
    # x = x.astype(int)
    # if DEBUG:
    #     print("x:", x)
    #     print("Ci:", np.dot(a, x))

    # In this approach, we round x to decimals=0
    x = np.round(x, 0)
    if DEBUG:
        print("Cr:", np.dot(a, x))

    if np.allclose(np.dot(a, x), c):
        return int(np.dot(x, costs))

    return 0  # if no solution


def solve(data, compute=compute):
    total = 0
    for i, m in enumerate(data):
        if DEBUG:
            print(f"=== Case {i} ====")
        cost = compute(m)
        if DEBUG:
            print(f"COST[{i}]\t{int(cost)}")
        total += int(cost)

    print(total)

    return total


def solve_p1(fpath = None):
    return solve(load(fpath), compute_with_numpy)


def solve_p2(fpath = None):
    return solve(load(fpath, task=2))


if __name__ == "__main__":
    solve_p1("test.1.txt") #=> 480
    solve_p1() #=> 29522

    #solve_p2("test.1.txt") #=> 875318608908?
    solve_p2() #=> 101214869433312
