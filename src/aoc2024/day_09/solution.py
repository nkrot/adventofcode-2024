#!/usr/bin/env python

from aoc2024 import load_input, from_env

DEBUG = from_env()


def load(fpath):
    return load_input(fpath, line_parser=parse_line)[0]


def parse_line(line: str) -> list[list[int]]:
    """
    Files and free space chunks alternate, being
    * even positions the files
    * odd positions the runs of free space
    """
    def to_id(pos: int) -> int:
        return -1 if pos % 2 else pos // 2

    values = list(map(int, line))
    segments = [
        [to_id(i), values[i]]
        for i in range(len(values))
    ]

    return segments


def defragment(disk: list[list[int]]):
    if DEBUG:
        print("defragment")
        print(f"DISK\t{disk}")

    defragmented = []

    while disk:

        # going from left to right, move files to `defragmented`.
        # this will stop just in front of a free space
        while disk and disk[0][0] > -1:
            defragmented.append(disk.pop(0))

        # going from right to left, remove all free spaces.
        # this will stop when the last segment is a file
        while disk and disk[-1][0] == -1:
            disk.pop()  # or keep?

        # if there is at least one free space and one file...
        if len(disk) > 1:
            space = disk.pop(0)
            file = disk.pop()

            if DEBUG:
                print(f"SPACE\t{space}")
                print(f"FILE\t{file}")

            # decide how much blocks of file we can move
            movable = min(space[1], file[1])
            # and move this many blocks to current free space
            if movable:
                defragmented.append([file[0], movable])
                space[1] -= movable
                file[1] -= movable

            # if current free space segment has free space left, readd it
            # back so that it can be used at the next iteration
            if space[1]:
                disk.insert(0, space)
            # if current file has not been moved completely, readd it back
            # so that we can handle it again at the next iteration
            if file[1]:
                disk.append(file)

        if DEBUG:
            print(f"disk\t{disk}\n\t\t{defragmented}\n")

    return defragmented


def defragment_2(disk):
    """changes are made in place"""

    def find_space(amount: int, stop_at: int) -> int:
        for idx in range(len(disk)-1, stop_at, -1):
            if disk[idx][0] == -1 and disk[idx][1] >= amount:
                return idx

    # reverse the list because the end of the list may grow larger when
    # segments with remaining free space are added.
    disk.reverse()

    if DEBUG:
        print("defragment_2")
        print(f"DISK (rev)\t{disk}")

    for lidx in range(0, len(disk)):
        if disk[lidx][0] == -1:  # is free space
            continue

        file = disk[lidx]
        if DEBUG:
            print("FILE", lidx, file)

        ridx = find_space(disk[lidx][1], lidx)
        if ridx is not None:
            space = disk[ridx]
            if DEBUG:
                print("SPACE", ridx, space)

            still_free_space = space[1] - file[1]

            # move file to free space
            space[0] = file[0]
            space[1] = file[1]

            # convert file to free space
            file[0] = -1

            if still_free_space:
                disk.insert(ridx, [-1, still_free_space])

    disk.reverse()
    return disk


def compute_checksum(disk) -> int:
    """
    To calculate the checksum, add up the result of
    multiplying each of these blocks' position with the file ID number it contains.
    The leftmost block is in position 0.
    If a block contains free space, skip it instead.
    """
    chks = 0
    pos = -1
    for segm in disk:
        for _ in range(segm[1]):
            pos += 1
            if segm[0] > 0:
                chks += pos*segm[0]
    return chks


def solve_p1(fpath = None):
    disk = load(fpath)
    degfragmented = defragment(disk)
    res = compute_checksum(degfragmented)
    print(res)
    return res


def solve_p2(fpath = None):
    disk = load(fpath)
    degfragmented = defragment_2(disk)
    res = compute_checksum(degfragmented)
    print(res)
    return res


if __name__ == "__main__":
    solve_p1("test.1.txt") #=> 1928
    solve_p1() #=> 6291146824486

    solve_p2("test.1.txt") #=> 2858
    solve_p2() #=> 6307279963620
