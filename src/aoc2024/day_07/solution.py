#!/usr/bin/env python

from aoc2024 import load_input, from_env
from aoc2024.day_07.common import parse_line, evaluate

DEBUG = from_env()

def can_be_true(equation, operators) -> bool:

    expected, operands = equation
    if DEBUG or True:
        print(f"Evaluating: {expected} == {operands}")

    return can_be_true_rec(expected, operands, operators)


def can_be_true_rec(expected, operands, operators) -> bool:
    """Recursive algorithm"""

    if len(operands) == 1:
        return operands[0] == expected

    return any(
        can_be_true_rec(
            expected,
            [evaluate(op, *operands[0:2])] + operands[2:],
            operators
        )
        for op in operators
    )


def solve(fpath, operators):
    equations = load_input(fpath, line_parser=parse_line)

    true_equations = [
        eqt
        for eqt in equations
        if can_be_true(eqt, operators)
    ]
    print("True equations", len(true_equations))

    res = sum(eqt[0] for eqt in true_equations)
    print(res)

    return res


def solve_p1(fpath = None):
    return solve(fpath, ('+', '*'))


def solve_p2(fpath = None):
    return solve(fpath, ('+', '*', '||'))


if __name__ == "__main__":
    solve_p1("test.1.txt") #=> 3749
    solve_p1() #=> 850435817339; 302 true equations

    solve_p2("test.1.txt") #=> 11387
    solve_p2() #=> 104824810233437; 501 true equations
