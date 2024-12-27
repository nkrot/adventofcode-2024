
import pytest

from aoc2024.day_17.solution import solve_p1, solve_p2

def test_solve_p1_1(tdata_1):
    actual = solve_p1(tdata_1.path)
    assert tdata_1.expected_p1 == actual

def test_solve_p2_2(tdata_2):
    actual = solve_p2(tdata_2.path)
    assert tdata_2.expected_p2 == actual

def test_solve_p1_real(tdata_real):
    actual = solve_p1(tdata_real.path)
    assert tdata_real.expected_p1 == actual

@pytest.mark.xfail(reason="Not solved yet")
def test_solve_p2_real(tdata_real):
    actual = solve_p2(tdata_real.path)
    assert tdata_real.expected_p2 == actual


# def test_1():
#     """
#     If register C contains 9, the program 2,6 would set register B to 1.
#     """
#     print("--- Test 1 ---")
#     registers = {"C": 9, "POINTER": 0}
#     execute(2, 6, registers)
#     print(registers)
#     assert 1 == registers["B"]
#
#
# def test_2():
#     """
#     If register A contains 10, the program 5,0,5,1,5,4 would output 0,1,2.
#     """
#     print("--- Test 2 ---")
#     registers = {"A": 10, "POINTER": 0}
#
#     execute(5, 0, registers)
#     execute(5, 1, registers)
#     execute(5, 4, registers)
#
#     print(registers)
#     assert "0,1,2" == prynt(registers)
#
# def test_3():
#     """
#     If register A contains 2024, the program 0,1,5,4,3,0 would output 4,2,5,6,7,7,7,7,3,1,0 and leave 0 in register A.
#     """
#     print("--- Test 3 ---")
#     registers = {"A": 10, "POINTER": 0}
#
#     execute(0, 1, registers)
#     execute(5, 4, registers)
#     execute(3, 0, registers)
#
#     print(registers)
#     assert "4,2,5,6,7,7,7,7,3,1,0" == prynt(registers)
#     assert 0 == registers["A"]
#
# def test_4():
#     """
#     If register B contains 29, the program 1,7 would set register B to 26.
#     """
#     print("--- Test 4 ---")
#     registers = {"B": 29, "POINTER": 0}
#
#     execute(1, 7, registers)
#
#     print(registers)
#     assert 26 == registers["B"]
#
# def test_5():
#     """
#     If register B contains 2024 and register C contains 43690, the program 4,0 would set register B to 44354.
#     """
#     print("--- Test 5 ---")
#     registers = {"B": 2024, "C": 43690, "POINTER": 0}
#
#     execute(4, 0, registers)
#
#     print(registers)
#     assert 44354 == registers["B"]
