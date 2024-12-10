#!/usr/bin/env python

from aoc2024 import load_input


def parse_line(line: str) -> list[int]:
    return list(map(int, line.strip().split()))


def is_safe(report: list[int]) -> bool:
    """
    A report is safe if
    1) The levels are either all increasing or all decreasing.
    2) Any two adjacent levels differ by at least one and at most three.
    """
    diffs = [a - b for a, b in zip(report, report[1:])]

    signs = [1 if n > 0 else -1 for n in diffs]
    if abs(sum(signs)) != len(signs):
        return False

    valid_diffs = [0 < abs(n) < 4 for n in diffs]

    return all(valid_diffs)


def is_safe_with_problem_dampener(report: list[int]) -> bool:
    return (
        is_safe(report)
        or
        any(map(is_safe, drop_one_level(report)))
    )


def drop_one_level(items: list):
    for idx in range(len(items)):
        shorter = items[:idx] + items[idx+1:]
        yield shorter


def solve_p1(fpath: str, safety_checker = is_safe):
    reports = load_input(fpath, line_parser=parse_line)
    safe_reports = list(filter(safety_checker, reports))
    res = len(safe_reports)
    print(res)

    return res


def solve_p2(fpath: str):
    return solve_p1(fpath, is_safe_with_problem_dampener)


if __name__ == "__main__":
    solve_p1("test.1.txt") #=> 2
    solve_p1("input.txt") #=> 299

    solve_p2("test.1.txt") #=> 4
    solve_p2("input.txt") #=> 364
