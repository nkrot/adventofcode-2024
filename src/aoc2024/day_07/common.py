import re

def parse_line(line: str) -> tuple[int, list[int]]:
    words = list(map(int, re.split(r"\D+", line)))
    return (words[0], words[1:])


def evaluate(op: str, l: int, r: int) -> int:
    if op == "+":
        v = l + r
    elif op == "*":
        v = l * r
    elif op == "||":
        v = int(str(l) + str(r))
    return v
