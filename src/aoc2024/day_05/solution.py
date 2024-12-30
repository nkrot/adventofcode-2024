#!/usr/bin/env python

import functools
import dataclasses

from aoc2024 import load_input, from_env, to_numbers

DEBUG = from_env()


@dataclasses.dataclass
class OrderedPage:
    """Used in part 2"""
    page: int
    followed_by: list[int]

    def __lt__(self, other: "OrderedPage"):
        return other.page in self.followed_by


def load(fpath = None):
    return load_input(fpath, by_blocks=True, line_parser=to_numbers)


def is_ordered_correctly(
    update: list[int],
    ordering_rules: list[list[int]],
):
    for i in range(len(update)-1):
        for j in range(1+i, len(update)):
            pair = [update[i], update[j]]
            if pair not in ordering_rules:
                return False
    return True


def compute_sum(updates: list[list[int]]) -> int:
    """
    Sum middle page numbers from each update
    """
    return sum(map(lambda upd: upd[len(upd)//2], updates))


def reorder_pages(update, ordering_rules) -> list[int]:
    """Reorder pages in `update` to comply with page ordering rules"""
    if DEBUG:
        print(f"REORDER:\t{update}")

    # simple and clear
    # followed_by = defaultdict(list)
    # for r in ordering_rules:
    #     followed_by[r[0]].append(r[1])

    # sophisticated and coprophagic, hence pythonic
    followed_by = functools.reduce(
        lambda acc, rule: (acc.setdefault(rule[0], []).append(rule[1]), acc)[1],
        ordering_rules,
        {}
    )
    if DEBUG:
        for p, pages in followed_by.items():
            print(f"{p} -> {pages}")

    reordered = sorted(
        update,
        key=lambda n: OrderedPage(n, followed_by.get(n, []))
    )

    if DEBUG:
        print(f"REORDERED:\t{reordered}\n")

    return reordered


def solve_p1(fpath = None):
    page_ordering_rules, updates = load(fpath)

    correct_updates = filter(
        lambda upd: is_ordered_correctly(upd, page_ordering_rules),
        updates
    )

    res = compute_sum(correct_updates)
    print(res)

    return res


def solve_p2(fpath = None):
    page_ordering_rules, updates = load(fpath)

    reordered = [
        reorder_pages(upd, page_ordering_rules)
        for upd in updates
        if not is_ordered_correctly(upd, page_ordering_rules)
    ]

    res = compute_sum(reordered)
    print(res)

    return res


if __name__ == "__main__":
    solve_p1("test.1.txt") #=> 143 (= 61+53+29)
    solve_p1() #=> 5208

    solve_p2("test.1.txt") #=> 123 (= 47+29+47)
    solve_p2() #=> 6732
