G1 = [
    [0, 1, 1, 1, 1],
    [1, 0, 1, 0, 0],
    [1, 1, 0, 0, 0],
    [1, 0, 0, 0, 1],
    [1, 0, 0, 1, 0],
]

G2 = [
    [0, 1, 1, 1, 0],
    [1, 0, 1, 0, 0],
    [1, 1, 0, 0, 0],
    [1, 0, 0, 0, 1],
    [0, 0, 0, 1, 0],

]

G3 = [
    [0, 1, 1, 1, 1],
    [1, 0, 1, 1, 0],
    [1, 1, 0, 0, 0],
    [1, 1, 0, 0, 1],
    [1, 0, 0, 1, 0],
    ]

G4 = [
    [0, 1, 1, 1, 0],
    [1, 0, 1, 1, 0],
    [1, 1, 0, 0, 0],
    [1, 1, 0, 0, 0],
    [0, 0, 0, 0, 0],
    ]


import networkx as nx
import numpy as np

G1 = nx.from_numpy_matrix(np.matrix(G1))
G2 = nx.from_numpy_matrix(np.matrix(G2))
G3 = nx.from_numpy_matrix(np.matrix(G3))
G4 = nx.from_numpy_matrix(np.matrix(G4))



def find_path(graph):
    if not nx.is_connected(graph):
        return "Graph not connected"
    if nx.is_eulerian(graph):
        return list(nx.eulerian_circuit(graph))
    if nx.is_semieulerian(graph):
        return list(nx.eulerian_path(graph))
    graph = nx.eulerize(graph)
    return list(nx.eulerian_circuit(graph))

print(find_path(G1))
print(find_path(G2))
print(find_path(G3))
print(find_path(G4))



