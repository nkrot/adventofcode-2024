#!/usr/bin/env python

# # #
#
#

from collections import deque

from aoc2024 import load_input, from_env

DEBUG = from_env()


def get_secret_number(secret):
    base = 16777216
    secret = (secret *   64 ^ secret) % base
    secret = (secret //  32 ^ secret) % base
    secret = (secret * 2048 ^ secret) % base
    return secret


def solve_p1(fpath = None):
    secrets = load_input(fpath, line_parser=int)

    for _ in range(2000):
        secrets = [
            get_secret_number(secret)
            for secret in secrets
        ]

    res = sum(secrets)
    print(res)

    return res


def solve_p2(fpath = None):
    """
    Runtime (user) on real input
    ----------------------------
            | python | pypy
    initial | 25,28  | 51,11
    deque   | 26,48  | 43,07
    +dict   | 6,58   | 6.97

    """

    buyers = load_input(fpath, line_parser=int)
    price_changes = [deque(maxlen=4) for _ in buyers]
    price_change_seqs = {}

    max_t = 2000
    for t in range(max_t):
        # print(f"Time: {t}")
        for idx in range(len(buyers)):
            secret = buyers[idx]
            buyers[idx] = get_secret_number(secret)
            #print(idx, buyers[idx])  # all unique
            #print(buyers[idx]) # some numbers repeat upto 5 times, most of them occur once

            price_change = (buyers[idx] % 10) - (secret % 10)
            price_changes[idx].append(price_change)

            if t >= 3:
                # print(t, idx, list(price_changes[idx]))
                # print(list(price_changes[idx]))
                seq = "({})".format(",".join(map(str, price_changes[idx])))

                # using here a dictionary in RHS gives a huge speed boost
                seqs = price_change_seqs.setdefault(seq, {})
                if idx not in seqs:
                    seqs[idx] = buyers[idx] % 10

                # Alternative: and this is slow:
                # seqs = price_change_seqs.setdefault(seq, [None] * len(buyers))
                # if seqs[idx] is None:
                #     seqs[idx] = buyers[idx] % 10

    def largest_sum(kv):
        return sum(filter(bool, kv[1].values()))

    max_pair = max(price_change_seqs.items(), key = largest_sum)
    # print(max_pair)
    res = sum(filter(bool, max_pair[1].values()))
    print(res)

    return res


if __name__ == "__main__":
    solve_p1("test.1.txt") #=> 37327623
    solve_p1() #=> 20332089158

    solve_p2("test.2.txt") #=> 23
    solve_p2() #=> 2191
