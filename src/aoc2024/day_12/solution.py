#!/usr/bin/env python

from dataclasses import dataclass
from collections import defaultdict
import functools

from aoc2024 import load_input, from_env, matrix as m, vector as vc

DEBUG = from_env()

@dataclass
class Plot:
    plant: str
    region_id: int = 0
    perimeter: int = 4

    def __iter__(self):
        return iter([self.plant, self.region_id, self.perimeter])


def mark_region(garden, xy, region_id = 0) -> bool:
    """
    Mark a single region by detecting adjacent plots with the same plant.
    It works in DFS fashion.
    Additionally, update perimeter.

    Returns
    -------
    True if region has been marked
    False if nothing new was marked
    """

    plot = m.value_at(garden, xy)
    if DEBUG:
        print(f"mark region as {region_id}: {xy} = {plot}")

    if plot.region_id != 0:
        if DEBUG:
            print(f"..skip, already marked as {plot.region_id}")
        return False

    plot.region_id = region_id

    for nxy, nplot in m.around(garden, xy):
        if plot.plant == nplot.plant:
            mark_region(garden, nxy, region_id)
            plot.perimeter -= 1

    return True


def mark_regions(garden):
    """
    Update garden plots in place by assigning Plot.region_id.
    All garden plots belonging to a single region will have the same
    Plot.region_id (int).

    Additionally, update Plot.perimeter.
    """
    region_id = 1
    for xy in m.scan(garden):
        if mark_region(garden, xy, region_id):
            region_id += 1


def compute_price_of_fence(garden):
    """ For part 1 """
    regions = defaultdict(list)

    for _, plot in m.scan(garden, with_value=True):
        regions[plot.region_id].append(plot.perimeter)

    return functools.reduce(
        lambda s, r: s + len(r) * sum(r),
        regions.values(),
        0
    )


def compute_price_of_fence_with_discount(garden):
    """
    For part 2.

    The number of sides is the number of corners a region has.
    Both inner and outer corners are counted.

    For each plot four corners are explored to check if they are corners
    of the whole region, located at NW, NE, SE, SW of the plot.
    To detect if a plot corner is a region corner, we explore 3 neighboring
    pieces located at offsets in `neighboring_corner_offsets` and compare
    them to the current plot. Inner and Outer corners have a different
    pattern of neighboring plots: see `corner_masks`
    """

    neighboring_corner_offsets = [
        (m.N, m.NE, m.E),
        (m.E, m.SE, m.S),
        (m.S, m.SW, m.W),
        (m.W, m.NW, m.N)
    ]

    corner_masks = [
        # True if neighboring plot belongs to the same region
        # False otherwise
        (True, False, True),   # inner corner
        (False, False, False), # outer corner
        (False, True, False),  # outer corner touching another outer corner
                               # of the same region (see test.5.txt)
    ]

    def count_corners(xy):
        curr = m.value_at(garden, xy)
        if DEBUG:
            print(f"count_corners of {xy} = {curr}")

        n_corners = 0
        for offsets in neighboring_corner_offsets:
            # get the neighboring pieces that are relevant for the corner
            # analysis
            neighbors = [
                m.value_at(garden, vc.add(xy, dxy))
                for dxy in offsets
            ]

            # mask is a comparison of the current piece to the three pieces
            # around it.
            mask = tuple(
                isinstance(nei, Plot) and nei.region_id == curr.region_id
                for nei in neighbors
            )
            if DEBUG:
                print("3 neighbors", neighbors)
                print("mask", mask)

            if mask in corner_masks:
                if DEBUG:
                    print("...is region corner")
                n_corners += 1

        return n_corners

    sides = defaultdict(list)

    for xy, plot in m.scan(garden, with_value=True):
        sides[plot.region_id].append(count_corners(xy))

    return functools.reduce(
        lambda s, r: s + len(r) * sum(r),
        sides.values(),
        0
    )


def solve_p1(fpath = None, compute_price = compute_price_of_fence):
    garden = m.load(fpath, as_type=Plot)
    mark_regions(garden)

    res = compute_price(garden)
    print(res)

    return res


def solve_p2(fpath = None):
    return solve_p1(fpath, compute_price_of_fence_with_discount)


if __name__ == "__main__":
    solve_p1("test.1.txt") #=> 140
    solve_p1() #=> 1377008

    solve_p2("test.1.txt") #=> 80
    solve_p2("test.5.txt") #=> 368
    solve_p2() #=> 815788
