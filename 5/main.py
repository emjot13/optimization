import networkx as nx
import numpy as np
from matplotlib import pyplot as plt
import copy

def is_eulerian(graph):
    odd = 0
    for node in graph:
        if sum(node) % 2 != 0:
            odd += 1
    if odd == 0:
        return "e"
    if odd == 2:
        return "s"
    return "n"



def findpath(graph, type):
    graph_copy = copy.deepcopy(graph)
    n = len(graph_copy)
    num_of_edges = []

    start_node = 0
    for index in range(len(graph_copy) - 1, -1, -1):
        if sum(graph_copy[index]) % 2 != 0:
            start_node = index

    for i in range(n):
        num_of_edges.append(sum(graph_copy[i]))
    stack = []
    path = []
    cur = start_node
    while (len(stack) > 0 or sum(graph_copy[cur]) != 0):
        if (sum(graph_copy[cur]) == 0):
            path.append(cur)
            cur = stack[-1]
            del stack[-1]
        else:
            for i in range(n):
                if (graph_copy[cur][i] == 1):
                    stack.append(cur)
                    graph_copy[cur][i] = 0
                    graph_copy[i][cur] = 0
                    cur = i
                    break
    if type == "s":
        path += find_shortest_path(graph, path[-1], path[0])[1:]
    else:
        path.append(path[0])
    for node in path:
        print(node, end = "-")
    print()
         

def dijkstra(graph, start, end=-1):
    number_of_nodes = len(graph)

    distances = [float('inf')] * number_of_nodes
    distances[start] = graph[start][start]  # 0

    visited = [False] * number_of_nodes
    parent = [-1] * number_of_nodes
    path = [{}] * number_of_nodes

    for count in range(number_of_nodes - 1):
        min = float("inf")
        u = 0
        for v in range(len(visited)):
            if visited[v] == False and distances[v] <= min:
                min = distances[v]
                u = v
        visited[u] = True
        for v in range(number_of_nodes):
            if not(visited[v]) and graph[u][v] != 0 and distances[u] + graph[u][v] < distances[v]:
                parent[v] = u
                distances[v] = distances[u] + graph[u][v]

    for i in range(number_of_nodes):
        j = i
        s = []
        while parent[j] != -1:
            s.append(j)
            j = parent[j]
        s.append(start)
        path[i] = s[::-1]
    return (distances[end], path[end]) if end >= 0 else (distances, path)

def find_shortest_path(graph, start, end=-1):
    return dijkstra(graph, start, end)[1]


def check(graph):
    G2_n = nx.from_numpy_matrix(np.matrix(graph))
    if not nx.is_connected(G2_n):
        print("graph not connected")
        return
    graph_type = is_eulerian(graph)
    print(graph_type)
    if graph_type != "n":
        findpath(graph, graph_type)
    nx.draw(G2_n, with_labels=True)
    plt.show()

def main():
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
    check(G1)
    check(G2)
    check(G3)
    check(G4)



main()










