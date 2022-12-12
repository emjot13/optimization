import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

import mst
import itertools

graph = [
    [0, 2, 6, 8, 4],
    [2, 0, 6, 7, 3],
    [6, 6, 0, 8, 5],
    [8, 7, 8, 0, 9],
    [4, 3, 5, 9, 0]
]

g = [
    [0, 5, 4],
    [5, 0, 10],
    [4, 10, 0]
]

def christofedes(graph):
    graph_as_nx = nx.from_numpy_matrix(np.matrix(graph))
    # print(nx.triangles(graph_as_nx))
    # print(graph_as_nx.edges.data())
    if not nx.is_connected(graph_as_nx):
        print("Graph is not connected")
        return
    triangles = {frozenset(x) for x in nx.enumerate_all_cliques(graph_as_nx) if len(x) == 3}
    indexes = [0, 1, 2]
    combinations = list(itertools.combinations(indexes, 2))
    for triangle in triangles:
        triangle = tuple(triangle)
        for c in combinations:
            x1 = triangle[[_ for _ in indexes if _ not in c][0]]
            x2 = triangle[c[0]]
            x3 = triangle[c[1]]
            if graph[x2][x3] > graph[x1][x2] + graph[x1][x3]:
                print("Triangle in-equality not satisfied")
                return

    minimal_spanning_tree = list([set(x) for x in mst.main(graph)])
    vertices = list(sum([tuple(x) for x in minimal_spanning_tree], ()))
    odd_vertices = list(set([vertex for vertex in vertices if vertices.count(vertex) % 2 == 1]))

    odd_vertices_graph = []

    for vertex in odd_vertices:
        v = []
        for i in range(len(graph)):
            if i in odd_vertices:
                v.append(graph[i][vertex])
        odd_vertices_graph.append(v)

    odd_vertices_graph_as_nx = nx.from_numpy_matrix(np.matrix(odd_vertices_graph))
    minimal_perfect_matching = [set(x) for x in nx.min_weight_matching(odd_vertices_graph_as_nx)]

    mst_minimal_perfect_matching_edges = minimal_spanning_tree + minimal_perfect_matching

    H = nx.MultiGraph()

    for edge in mst_minimal_perfect_matching_edges:
        edge = sorted(tuple(edge))
        v1, v2 = edge[0], edge[1]
        H.add_edge(v1, v2, weight=graph[v1][v2])

    eulerian_cycle = list(nx.eulerian_circuit(H))
    hamilton_cycle = set(frozenset(x) for x in eulerian_cycle)

    total_weight = 0
    for edge in hamilton_cycle:
        edge = tuple(edge)
        v1, v2 = edge[0], edge[1]
        print(f"{v1} -> {v2}")
        total_weight += graph[v1][v2]

    print(f"weight of cycle: {total_weight}")


christofedes(graph)