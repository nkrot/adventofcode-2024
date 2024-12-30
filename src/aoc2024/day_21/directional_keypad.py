from typing import Iterator

import networkx as nx

from . import utils

#     +---+---+
#     | ^ | A |
# +---+---+---+
# | < | v | > |
# +---+---+---+

KEYPAD = nx.DiGraph()

KEYPAD.add_edges_from([
    ("v", "^", {"d": "^"}),
    ("v", ">", {"d": ">"}),
    ("v", "<", {"d": "<"}),

    ("<", "v", {"d": ">"}),

    (">", "v", {"d": "<"}),
    (">", "A", {"d": "^"}),

    ("^", "v", {"d": "v"}),
    ("^", "A", {"d": ">"}),

    ("A", "^", {"d": "<"}),
    ("A", ">", {"d": "v"}),
])


def press(src, trg, g = KEYPAD) -> Iterator[str]:
    return (p + "A" for p in utils.path_to(src, trg, g))


def type_code(code: str, start: str = "A") -> Iterator[str]:
    yield from utils.type_code(
        code,
        start,
        lambda src, trg: press(src, trg, KEYPAD)
    )
