#!/usr/bin/env python

import networkx as nx

from aoc2024 import load_input, from_env

DEBUG = from_env()

def has_t(nodes):
    return any(n[0] == "t" for n in nodes)


def solve_p1(fpath = None):
    pairs = load_input(fpath, line_parser=lambda s: sorted(s.split('-')))

    lan = {}
    for u, v in pairs:
        lan.setdefault(u, []).append(v)

    # sorting aims at avoiding duplicates when considering pairs of nodes
    # further.
    for u in lan:
        lan[u] = sorted(lan[u])

    triples = []
    for u, vs in lan.items():
        # check each pair of child nodes of u for if child 1 (vs[i]) has
        # child 2 (vs[j]) as its own child.
        c_vs = len(vs)
        for i in range(c_vs-1):
            for j in range(i+1, c_vs):
                if vs[j] in lan.get(vs[i], []):
                    triple = (u, vs[i], vs[j])
                    if has_t(triple):
                        triples.append(triple)

    if DEBUG:
        triples.sort()
        for triple in triples:
            print(triple)

    res = len(triples)
    print(res)

    return res


def solve_p1_v2(fpath = None):
    """
    The algorithm is the same as in version 1.
    The backbone data structure is a networkx.Graph.
    """
    lan = load(fpath)

    def neighbors(node):
        return set(filter(lambda u: u > node, nx.neighbors(lan, node)))

    triples = set()
    for u in lan.nodes():
        vs = neighbors(u)
        for v in vs:
            common = vs & neighbors(v)
            if common:
                triples.update(filter(has_t, [
                    (u, v, c)
                    for c in common
                ]))

    if DEBUG:
        for triple in triples:
            print(sorted(triple))

    cnt = len(triples)
    print(cnt)

    return cnt


def load(fpath = None) -> nx.Graph:
    edges = load_input(fpath, line_parser=lambda s: s.split("-"))
    g = nx.Graph()
    g.add_edges_from(edges)
    return g


def solve_p2(fpath = None):
    """
    Solution is based on finding cliques in a graph
    https://networkx.org/documentation/stable/reference/algorithms/clique.html
    """
    lan = load(fpath)
    subnet = max(nx.find_cliques(lan), key=len)
    password = ",".join(sorted(subnet))
    print(password)

    return password


if __name__ == "__main__":
    solve_p1("test.1.txt") #=> 7
    solve_p1() #=> 1077

    solve_p2("test.1.txt") #=> "co,de,ka,ta"
    solve_p2() #=> "bc,bf,do,dw,dx,ll,ol,qd,sc,ua,xc,yu,zt"
