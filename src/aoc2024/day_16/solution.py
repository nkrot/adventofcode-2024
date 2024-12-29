#!/usr/bin/env python

import queue
import operator
from collections import deque
from dataclasses import dataclass, field
from functools import reduce

from aoc2024 import from_env, matrix as m, vector as vct, maze as mz

DEBUG = from_env()


@dataclass
class Reindeer:
    xy: tuple[int, int]
    facing: tuple[int, int]
    score: int = 0
    path: set = field(default_factory=set)


@dataclass
class PrioritizedReindeer:
    data: Reindeer

    def __lt__(self, other: Reindeer):
        return self.data.score < other.data.score


def load(fpath = None):
    maze, start, end = mz.load(fpath, pois="SE")
    reindeer = Reindeer(start, m.RIGHT)
    # m.set_value_at(maze, end, ".")

    if DEBUG:
        m.print(maze)
        print(reindeer, "End=", end)

    return maze, reindeer, end


def move(rd: Reindeer, xy: tuple[int, int]) -> Reindeer:
    """Move reindeer to new position xy.
    Assuming (w/o validation) that target xy is a neighboring position

    Returns
    -------
    new Reindeer
    """
    # print("Before:", rd)
    new_rd = Reindeer(
        xy,
        vct.sub(xy, rd.xy),
        rd.score+1,
        #rd.path | {rd.xy}
        list(rd.path) + [rd.xy],
    )

    # update the score due to turning
    if new_rd.facing != rd.facing:
        diff = vct.mul(new_rd.facing, rd.facing)
        # (0,0) means 1 turn of 90 degrees
        # (0,-1) or (-1,0) means 2 turns of 90 degrees each
        # (1,0) or (0,1) means 0 or 3 turns (no change of direction)

        # Initially not clear how to count a turn:
        # a) every 90 degree turn counts as 1000?
        # b) a turn of any degree (90, 180, 270) counts as 1000?
        #cost = (1 - sum(diff)) * 1000 # (a)
        cost = 0 if sum(diff) == 1 else 1000 # (b)
        # print("Turn", rd.facing, new_rd.facing, diff, cost)
        new_rd.score += cost

    # print("After :", new_rd)
    return new_rd


def wall_up_dead_ends(maze):
    """Find dead ends (and corridors leading to them) and fill them
    with the character =

    Initially developed for purposes of debugging. It affects performance
    (runtime) slightly.
    """
    c_finds = 0
    changed = True
    i = 0
    while changed:
        i += 1
        changed = False
        # print(f"Closing dead ends: {i}")
        for xy, v in m.scan(maze, with_value=True):
            if v == ".":
                nei = "".join(nv for _, nv in m.around(maze, xy) if nv in "#=" )
                if len(nei) == 3:
                    # three neighors are either # or =
                    3 == sum(nv in "#=" for _, nv in m.around(maze, xy))
                    # print(xy, v, nei)
                    m.set_value_at(maze, xy, "=")
                    c_finds += 1
                    changed = True

    def to_str(row):
        return "".join(row).replace(".", " ")

    if DEBUG:
        print(f"Dead-ends: {c_finds}")
        m.print(maze, row_hook=to_str)


def find_path(maze, deer, find_all=False) -> list[Reindeer]:
    """
    It uses priority queue where the priority is the score accumulated so far
    is the priority.
    """

    cmp = operator.gt if find_all else operator.ge

    def qpush(deer):
        deers.put(PrioritizedReindeer(deer)) # 1
        #deers.append(deer) # 2

    def qpop():
        return deers.get().data #1
        #return deers.popleft() #2.1 bfs, faster than 2.2/dsf
        #return deers.pop()  #2.2 dsf

    def qsize():
        return deers.qsize() # 1
        #return len(deers) # 2

    deers = queue.PriorityQueue() # 1, works pretty fast
    #deers = deque() # 2 is slower that PriorityQueue. finds same result
    qpush(deer)

    finds = []
    min_score = 0
    min_scores = {}
    while qsize() > 0:
        # print("Queue size:", qsize())
        curr = qpop()
        # print("At:", curr)
        for xy, val in m.around(maze, curr.xy):
            if val in ".E":
                nei = move(curr, xy)
                # print("\t", xy, val, nei)

                # This seems to prune the same paths as the rule below that
                # prunes by local min score.
                # if nei.xy in nei.path:
                #     # print(f"...skipping: already visited {len(nei.path)}")
                #     continue

                if min_score and cmp(nei.score, min_score):
                    # print(f"...skipping: too a high score ({nei.score} >= {min_score})")
                    continue

                #key = (curr.facing, nei.facing)
                #key = curr.facing
                key = nei.facing
                min_scores.setdefault(key, {})
                if nei.xy in min_scores[key] and cmp(nei.score, min_scores[key][nei.xy]):
                    # print(f"...skipping: local score too high: ({nei.score} >= {min_scores[key][nei.xy]})")
                    continue

                min_scores[key][nei.xy] = nei.score

                if val == "E":
                    # print("Found:", nei)
                    finds.append(nei)
                    min_score = min(nei.score, min_score) if min_score else nei.score
                else:
                    qpush(nei)

    finds = sorted(finds, key=lambda rd: rd.score)
    # print(f"Found: {len(finds)}")

    return finds if find_all else finds[0]


def draw_path(maze, path: list):
    """For debugging purposes"""
    for xy in path:
        m.set_value_at(maze, xy, "o")
    m.print(maze, row_hook="".join)

    print(f"path length: {len(path)}")
    deer = Reindeer(path[0], m.RIGHT)
    print(0, "-", deer)
    for idx in range(1, len(path)):
        score = deer.score
        deer = move(deer, path[idx])
        dir = "T" if deer.score - score > 1000 else "-"
        print(idx, dir, deer)


def solve_p1(fpath = None):
    maze, deer, end = load(fpath)
    # brick_up_dead_ends(maze)
    best_deer = find_path(maze, deer)
    # draw_path(maze, best_deer.path)
    print(best_deer.score)

    return best_deer.score


def solve_p2(fpath = None):
    maze, deer, end = load(fpath)
    # brick_up_dead_ends(maze)
    deers = find_path(maze, deer, find_all=True)
    # Find all paths and compute the number of unique tiles in all of them
    tiles = reduce(lambda acc, rd: acc.union(rd.path), deers, set())
    res = 1+len(tiles)
    print(res)

    return res


if __name__ == "__main__":
    solve_p1("test.1.txt") #=> 7036
    solve_p1("test.2.txt") #=> 11048
    # solve_p1("test.3.txt") #=> my, 2011
    solve_p1() #=> 94436

    solve_p2("test.1.txt") #=> 45
    solve_p2("test.2.txt") #=> 64
    solve_p2() #=> 481
