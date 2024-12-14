#!/usr/bin/env python

# # #
# UNFINISHED
# p.1 works for all inputs
# p.2 works for test inputs but fails for real input

from typing import Optional
from aoc2024 import load_input, from_env, matrix as m, vector as vct

DEBUG = from_env()


def load(fpath = None, task: int = 1):

    mapping = {
        "<": m.LEFT,
        ">": m.RIGHT,
        "^": m.UP,
        "v": m.DOWN
    }

    mapping_task2 = {
        "O": "[]",
        "@": "@.",
        "#": "##",
        ".": "..",
    }

    def parse_line(line):
        if task == 2 and line.startswith("#"):
            # make the maze 2x wider
            row = [
                list(mapping_task2.get(v))
                for v in line
            ]
            # return row # 3D
            return sum(row, []) # 2D

        return [
            mapping.get(v, v)
            for v in line
        ]

    maze, moves = load_input(fpath, by_blocks=True, line_parser=parse_line)

    robot, _ = m.find(maze, "@")
    moves = sum(moves, [])

    # m.print(maze, header="--- warehouse ---")
    # print("robot", robot)
    # print()
    # print("moves", moves)

    return maze, robot, moves


def move(warehouse, src_xy, direction):
    """
    Warehouse is updated in place

    Returns
    -------
    ???
    """

    def at(xy):
        return m.value_at(warehouse, xy)

    def move_cell(src_xy, dest_xy):
        m.set_value_at(warehouse, dest_xy, at(src_xy))
        m.set_value_at(warehouse, src_xy, ".")

    dest_xy = vct.add(src_xy, direction)  # destination xy

    if at(dest_xy) == "O":  # a box
        # try moving the box away in the requested direction
        # if moving succeeds, src_xy will become "." and we will see it later.
        move(warehouse, dest_xy, direction)

    if at(dest_xy) == ".":  # empty space
        move_cell(src_xy, dest_xy)
        return dest_xy

    return src_xy


def move2(warehouse, robot, direction):
    """ move() for task 2"""

    def at(xy):
        return m.value_at(warehouse, xy)

    def get_box_at(xy) -> Optional[list]:
        """A box has two edges. Find them and return as a list
            [left edge, right edge]
        If there is no box at this position `xy`, return None
        """
        box = []
        v = at(xy)
        if v == "]":
            box = [vct.add(xy, m.LEFT), xy]
        elif v == "[":
            box = [xy, vct.add(xy, m.RIGHT)]
        if box:
            # validate it to catch errors
            vv = "".join(at(xy) for xy in box)
            if vv == "[]":
                return box
            else:
                raise RuntimeError(f"Not a box at {box} having {vv}")

    def move_cell(src_xy, dest_xy):
        m.set_value_at(warehouse, dest_xy, at(src_xy))
        m.set_value_at(warehouse, src_xy, ".")

    def move_box(box, direction):
        dest = [vct.add(edge, direction) for edge in box]
        things = "".join(at(edge) for edge in dest)
        if DEBUG:
            print(f"..move box {box} -> {dest} being {things}")

        # move away any boxes that are at destination
        if direction == m.LEFT and things[0] != ".":
            move_box(dest, direction)

        if direction == m.RIGHT and things[1] != ".":
            move_box(dest, direction)

        if direction in {m.UP, m.DOWN} and things != "..":
            if things == "][":
                move_box(get_box_at(dest[0]), direction)
                move_box(get_box_at(dest[1]), direction)
            elif things == "].":
                move_box(get_box_at(dest[0]), direction)
            elif things == ".[":
                move_box(get_box_at(dest[1]), direction)
            elif things == "[]":
                move_box(dest, direction)
            else:
                raise NotImplementedError(f"Not yet for {direction} {things}")

        # when moving to the right, we need to consider box sides in reverse
        # order to avoid overwriting the other side
        if direction == m.RIGHT and at(dest[1]) == ".":
            move_cell(box[1], dest[1])
            move_cell(box[0], dest[0])
        elif direction != m.RIGHT and at(dest[0]) == ".":
            move_cell(box[0], dest[0])
            move_cell(box[1], dest[1])

    def can_move_box(pts: list, direction) -> bool:
        """Check if a pair of points `pts` can be moved in requested `direction`.
        A box is given as a list of edges.
        """
        if pts is None:
            return False

        dest = [vct.add(xy, direction) for xy in pts]
        things = [at(xy) for xy in dest]

        if not all(things):  # off the matrix
            return False

        things = "".join(things)
        if direction == m.LEFT:
            return things[0] == "." or can_move_box(dest, direction)

        elif direction == m.RIGHT:
            return things[1] == "." or can_move_box(dest, direction)

        elif direction in {m.UP, m.DOWN}:
            #print(vv)
            if things == "..":
                return True
            elif things == ".[":
                return can_move_box(get_box_at(dest[1]), direction)
            elif things == "].":
                return can_move_box(get_box_at(dest[0]), direction)
            elif things == "[]":
                return can_move_box(dest, direction)
            elif things == "][":
                return (
                    can_move_box(get_box_at(dest[0]), direction)
                    and
                    can_move_box(get_box_at(dest[1]), direction)
                )
            # the below seems to work as well
            # else
            #     (things[0] == "." or can_move_box(get_box_at(dest[0]), direction))
            #     and
            #     (things[1] == "." or can_move_box(get_box_at(dest[1]), direction))
            # )

        return False

    if DEBUG:
        print(f"Move {robot} in {direction}")

    dest_xy = vct.add(robot, direction)
    box = get_box_at(dest_xy)
    if DEBUG:
        print(f"BOX at {dest_xy}: {box}")

    if box:
        if can_move_box(box, direction):
            if DEBUG:
                print(f"..box can be moved in {direction}")
            move_box(box, direction)
        else:
            if DEBUG:
                print(f"..box cannot be moved in {direction}")

    # move the robot
    if at(dest_xy) == ".":  # empty space
        move_cell(robot, dest_xy)
        return dest_xy

    return robot


def play(warehouse, robot, moves):
    for idx, mv in enumerate(moves):
        robot = move(warehouse, robot, mv)
        if DEBUG:
            print_warehouse(warehouse, f"--- After Step {idx}: {mv} ---")


def compute_gps(warehouse):
    gps = 0
    for (x,y), v in m.scan(warehouse, with_value=True):
        if v in "O[":
            gps += 100*x + y
    return gps


def solve_p1(fpath = None):
    warehouse, robot, moves = load(fpath)

    play(warehouse, robot, moves)
    if DEBUG:
        print(warehouse, "--- Final state ---")

    res = compute_gps(warehouse)
    print(res)

    return res


def print_warehouse(warehouse, header = ""):
    m.print(warehouse, header = header, row_hook=lambda row: "".join(row))


def solve_p2(fpath = None):
    warehouse, robot, moves = load(fpath, task=2)
    if DEBUG:
        print_warehouse(warehouse, "--- Initial ----")

    for idx, mv in enumerate(moves):
        robot = move2(warehouse, robot, mv)
        if DEBUG:
            print_warehouse(warehouse, f"--- After Step {idx}: {mv} ---")

    if DEBUG:
        print_warehouse(warehouse, "--- Final state ---")

    res = compute_gps(warehouse)
    print(res)

    return res


if __name__ == "__main__":
    # solve_p1("test.1.txt") #=> 2028
    # solve_p1("test.2.txt") #=> 10092
    # solve_p1() #=> 1538871

    #solve_p2("test.3.txt") #=> 618
    #solve_p2("test.2.txt") #=> 9021
    solve_p2() #=> 1544530 too high

# expected for: test.3.txt
##############
##...[].##..##
##...@.[]...##
##....[]....##
##..........##
##..........##
##############

# expected for: test.2.txt
####################
##[].......[].[][]##
##[]...........[].##
##[]........[][][]##
##[]......[]....[]##
##..##......[]....##
##..[]............##
##..@......[].[][]##
##......[][]..[]..##
####################
