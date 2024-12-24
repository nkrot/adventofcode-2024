#!/usr/bin/env python

# # #
#
#

import os
import networkx as nx

from aoc2024 import load_input, from_env

DEBUG = from_env()


def load(fpath, task=1):
    g = nx.DiGraph()

    def _parse(line):
        # print(line)
        tokens = line.replace(':', '').split()
        if len(tokens) == 2:
            g.add_node(tokens[0], value=int(tokens[1]))
        elif len(tokens) == 5:
            src1, op, src2, _ , dest = tokens
            if dest in g:
                g.nodes[dest]["op"] = op
            else:
                g.add_node(dest, op=op)
            g.add_edges_from([(src1, dest), (src2, dest)])

        elif len(tokens):
            raise ValueError(f"Cannot parse line: '{line}'")

        return g

    load_input(fpath, line_parser=_parse)

    if DEBUG:
        outfile = "graph.{}.p{}.dot".format(
            os.path.basename(fpath or "input.txt"),
            task
        )
        write_graph_as_dotty(g, outfile)

    return g


def write_graph_as_dotty(g, outfile):
    """
    Write given graph in DOT format to output file

    For a more informative visualization in dot format, we need to
    convert our node attributes (value, op) to a label so that they are
    displayed.

    To display resulting graph
    > xdot outfile
    or generate PNG from dot file:
    > dot -Tpng outfile -o outfile.png
    """
    print(
        f"Writing graph to: {outfile}"
        f"To view the file, use 'xdot {outfile}'"
    )
    eg = nx.DiGraph(g)
    for n, data in eg.nodes(data=True):
        label = "\n".join(f"{k}={v}" for k,v in sorted(data.items()))
        eg.nodes[n]["label"] = f"{n}\n[{label}]"
    nx.nx_agraph.write_dot(eg, outfile)


def compute(g, node):
    attrs = g.nodes[node]
    if "value" not in attrs:
        left, right = list(g.predecessors(node))
        value = 0
        if attrs["op"] == "AND":
            value = compute(g, left) and compute(g, right)
        elif attrs["op"] == "OR":
            value = compute(g, left) or compute(g, right)
        elif attrs["op"] == "XOR":
            value = compute(g, left) ^ compute(g, right)
        attrs["value"] = value
    return attrs["value"]


def registers(g, initial = 'z', with_value=False) -> list[str]:
    """
    Find all nodes in graph `g` whose names start with `initial` and return
    them sorted from most significant to least significant digit:
    >>> nodes(g, 'x')
    finds all nodes: [x08, x07, ..., x00]
    """
    nodes = [n for n in g.nodes() if n.startswith(initial)]
    nodes = sorted(nodes, reverse=True)
    if with_value:
        nodes = [
            (n, g.nodes[n].get("value", "?"))
            for n in nodes
        ]
    return nodes


def init_registers(g, reg: str, bin: str):
    rs = registers(g, reg)

    if len(rs) != len(bin):
        raise ValueError(
            f"Length of {reg} value is not equal the number of registers: {bin} vs {rs}"
        )

    for r, v in zip(rs, bin):
        g.nodes[r]["value"] = int(v)
        # print(v, r, g.nodes[r])


def init(g, x: str, y: str):
    # remove all computed values
    for _, attrs in g.nodes(data=True):
        if "op" in attrs and "value" in attrs:
            del attrs["value"]

    init_registers(g, 'x', x)
    init_registers(g, 'y', y)


def run(g) -> list[int]:
    outputs = [compute(g, n) for n in registers(g, 'z')]
    return outputs


def solve_p1(fpath = None):
    g = load(fpath, 1)

    outputs = run(g)

    if DEBUG:
        outfile = "graph.{}.p1.res.dot".format(os.path.basename(fpath or "input.txt"))
        write_graph_as_dotty(g, outfile)
        print(f"OUTPUTS: {outputs}")

    res = int("".join(map(str, outputs)), 2)
    print(res)

    return res

def show_registers(g, names='xyz', header=None):
    if header is not None:
        print(header)
    for name in names:
        values = registers(g, name, with_value=True)
        print(f"{name}s: {values}")


def solve_p2(fpath = None):
    x = load_input(fpath)
    res = 1
    print(res)

    return res


if __name__ == "__main__":
    solve_p1("test.1.txt") #=> 4
    solve_p1("test.2.txt") #=> 2024
    solve_p1() #=> 69201640933606

    #solve_p2("test.1.txt") #=>
    #solve_p2() #=>
