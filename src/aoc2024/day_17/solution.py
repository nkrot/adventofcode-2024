#!/usr/bin/env python

import os

from aoc2024 import load_input, from_env

DEBUG = from_env()

def load(fpath = None):

    def _parse(line: str):
        tokens = line.split()
        if tokens[0] == "Register":
            return tokens[1][:-1], int(tokens[2])
        else:
            return list(map(int, tokens[1].split(",")))

    blocks = load_input(fpath, by_blocks=True, line_parser=_parse)

    registers = dict(blocks[0])
    program = blocks[1][0]

    registers.update({
        "OUT": [],
        "POINTER": 0,
    })

    if DEBUG:
        print("Registers:", registers)
        print("Program:", program)

    return registers, program


def prynt(registers, really=False):
    val = None
    if "OUT" in registers:
        val = ",".join(map(str, registers["OUT"]))
    if really:
        print(val)
    return val

def combo(code, registers):
    match code:
        case 0 | 1 | 2 | 3:
            return code
        case 4:
            return registers["A"]
        case 5:
            return registers["B"]
        case 6:
            return registers["C"]
        case 7:
            raise ValueError("Reserved and should not appear in valid programs")


def execute(opcode, operand, registers):
    registers["POINTER"] += 2
    match opcode:
        case 0:  # adv
            registers["A"] = registers["A"] // 2**combo(operand, registers)
        case 1:  # bxl
            registers["B"] = registers["B"] ^ operand
        case 2:  # bst
            registers["B"] = combo(operand, registers) % 8
        case 3:  # jnz
            if registers.get("A", 0):
                registers["POINTER"] = operand
        case 4:  # bxc
            registers["B"] = registers["B"] ^ registers["C"]
        case 5:  # out
            val = combo(operand, registers) % 8
            registers.setdefault("OUT", []).append(val)
        case 6:  # bdv
            registers["B"] = registers["A"] // 2**combo(operand, registers)
        case 7:  # cdv
            registers["C"] = registers["A"] // 2**combo(operand, registers)


def run(program, registers):
    # print("--- RUN ---")
    while registers["POINTER"] < len(program):
        ptr = registers["POINTER"]
        opcode, operand = program[ptr], program[1+ptr]
        if DEBUG:
            print(f"[{ptr}/{1+ptr}]: {opcode} {operand}")
        execute(opcode, operand, registers)
    # if DEBUG:
    #     print(registers)


def solve_p1(fpath = None):
    registers, program = load(fpath)
    run(program, registers)

    res = prynt(registers, True)

    return res


def solve_p2(fpath = None):
    if not fpath or os.path.basename(fpath) == "input.txt":
        return -1  # not solved yet

    registers, program = load(fpath)

    a = 10 ** (len(program)-2) - 1
    while registers["OUT"] != program:
        a += 1
        registers = {
            "A": a,
            "B": 0,
            "C": 0,
            "POINTER": 0,
            "OUT": []
        }

        run(program, registers)
        #print(a, prynt(registers))

    print(a)

    return a

# required
# Program: 2,4,1,3,7,5,4,0,1,3,0,3,5,5,3,0 -- 16

# hypothesys:
# If N is the number of digits in register A, then the output will be N+1
# in: 1000000001861692 - N=16
# out: 4,7,4,6,7,2,7,5,1,3,7,4,2,7,0,4,0  -- 17

# in: 100000000033294 - N=15 digits
# out: 6,1,1,1,3,6,6,0,2,3,3,7,5,7,6,3 - 16 digits

if __name__ == "__main__":
    solve_p1("test.1.txt") #=> 4,6,3,5,6,3,5,2,1,0
    solve_p1() #=> 1,5,7,4,1,6,0,3,0

    solve_p2("test.2.txt") #=> 117440
#    solve_p2() #=> not solved
