import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import itertools

adj_matrix = [
    [0, 4, 8, 2, 3],
    [4, 0, 2, 1, 0],
    [8, 2, 0, 0, 0],
    [2, 1, 0, 0, 7],
    [3, 0, 0, 7, 0],
]


def show_graph(graph):
    layout = nx.spring_layout(graph)
    labels = nx.get_edge_attributes(graph, "weight")
    nx.draw(graph, layout, with_labels=True)
    nx.draw_networkx_edge_labels(graph, pos=layout, edge_labels=labels)
    plt.show()


def get_odd_nodes(graph):
    odd_nodes = [node for node, degree in graph.degree() if degree % 2 == 1]
    return odd_nodes


def get_pairs(odd_nodes):
    odd_nodes_pairs = list(itertools.combinations(odd_nodes, 2))
    return odd_nodes_pairs


def shortest_path(graph, pairs):
    distances = {}
    for pair in pairs:
        u, v = pair[0], pair[1]
        distances[pair] = nx.dijkstra_path_length(graph, u, v, graph.get_edge_data(u, v).get("weight"))
    return distances

def get_complete_graph(pairs):
    complete_graph = nx.Graph()
    for pair, weight in pairs.items():
        u, v = pair[0], pair[1]
        complete_graph.add_edge(u, v, **{"weight": weight})
    return complete_graph

def change_original_graph(graph, min_weight_pairs):
    changed_graph = nx.Graph(graph.copy())
    for pair in min_weight_pairs:
        u, v = pair[0], pair[1]
        changed_graph.add_edge(u, v, **{"weight": nx.dijkstra_path_length(graph, u, v)})
    return changed_graph


def main():
    G = nx.from_numpy_matrix(np.matrix(adj_matrix))
    print(G.edges())
    odd_nodes = get_odd_nodes(G)
    pairs = get_pairs(odd_nodes)
    shortest_paths = shortest_path(G, pairs)
    # print(shortest_paths)
    complete_graph = get_complete_graph(shortest_paths)
    odd_pairs = nx.algorithms.max_weight_matching(complete_graph, True)
    changed_graph = change_original_graph(G, odd_pairs)
    print(changed_graph.edges())
    # print(odd_pairs)
    # print(complete_graph.nodes())
    # print(G.edges())
    # print(G.get_edge_data(1, 3))

main()