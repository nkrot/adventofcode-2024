from typing import Callable, Iterator

import networkx as nx


def path_to(source: str, target: str, g: nx.DiGraph) -> Iterator[str]:
    """
    generate shortest paths between nodes `source` and `target`
    in terms of moves < and >
    """
    def _convert(nodes: list[str]):
        return "".join(
            g.edges[s, t]["d"]
            for s, t in zip(nodes, nodes[1:])
        )

    for path in nx.all_shortest_paths(g, source, target):
        yield _convert(path)


def type_code(code: str, start: str, press: Callable) -> Iterator[str]:
    if code:
        for head in press(start, code[0]):
            for tail in type_code(code[1:], code[0], press):
                yield head + tail
    else:
        yield ""
