#!/usr/bin/env python

# # #
# extremely slow solution
# runnning for real inputs is DISABLED

import itertools
import operator
import functools

from aoc2024 import load_input, from_env
from aoc2024.day_07.common import parse_line, evaluate

DEBUG = from_env()

METHODS = {
    "+": "__add__",
    "*": "__mul__",
}

def evaluate_sequence(operands, operators, stop_if = None) -> int:
    """
    There is no precedence of operators. The sequence is left associative.
    """
    if DEBUG:
        print("evaluate_sequence", operands, operators)

    if len(operands) == 1:
        return operands[0]

    op = operators.pop(0)
    l = operands.pop(0)
    r = operands.pop(0)

    # These wort ok for standard operators + and *
    #v = eval(f"{l} {op} {r}")
    #v = getattr(l, METHODS[op])(r)

    v = evaluate(op, l, r)

    if stop_if and stop_if(v, f"{l} {op} {r}"):
        return v

    operands.insert(0, v)

    return evaluate_sequence(operands, operators, stop_if)


def combinations(items, length: int):
    """
    Generate all unique arrangements of items of given `length`.
    The constrain of uniqueness is satisfied iff `items` has all unique
    values, that is true for this very task.

    TODO:
    can this be cached?
    """
    for comb in itertools.combinations_with_replacement(items, length):
        yield from set(itertools.permutations(comb))


def can_be_true(equation, operators) -> bool:
    expected, operands = equation
    if DEBUG or True:
        print(f"Evaluating: {expected} == {operands}")

    def is_too_high(v, msg = None) -> bool:
        cmp = v > expected
        if cmp:
            print(f"..Too high {v} > {expected} (from: {msg})")
        return cmp

    # Optimization
    # the sum determines the lower and the product the upper bound of
    # the expression. If desired value is outside of this range, dont
    # bother testing

    lower = sum(operands)
    upper = functools.reduce(operator.mul, operands)

    # TODO: bug here?
    #if not(lower <= expected <= upper):  # something wrong here
    #   return False

    if True:
        for ops in combinations(operators, len(operands)-1):
            value = evaluate_sequence(list(operands), list(ops), is_too_high)
            if value == expected:
                return True

    return False


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
    """
    Runtime
    -------
    user 1286,32
    """
    return solve(fpath, ('+', '*'))


def solve_p2(fpath = None):
    """
    Runtime
    -------
    forgot to time it, wallclock time around 5hrs ?
    """
    return solve(fpath, ('+', '*', '||'))


if __name__ == "__main__":
    solve_p1("test.1.txt") #=> 3749
    #solve_p1() #=> 850435817339; 302 true equations

    solve_p2("test.1.txt") #=> 11387
    #solve_p2() #=> 104824810233437; 501 true equations
