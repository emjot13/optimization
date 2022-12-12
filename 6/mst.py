# można użyć wag w macierzy sąsiedztwa

import check_if_has_dfs_tree
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt


class Prim:
    def __init__(self, adj_matrix, start_vertex):
        self.adj_matrix = adj_matrix
        self.number_of_vertices = len(adj_matrix)
        self.start_vertex = start_vertex
        self.number_of_edges = 0
        self.selected_vertices = [False] * self.number_of_vertices

    def print_graph(self):
        node_labels = {_: _ for _ in range(self.number_of_vertices)}
        G = nx.from_numpy_matrix(np.matrix(self.adj_matrix), create_using=nx.Graph)
        layout = nx.spring_layout(G)
        nx.draw(G, layout, with_labels=True, labels=node_labels)
        edge_labels = nx.get_edge_attributes(G, "weight")
        nx.draw_networkx_edge_labels(G, pos=layout, edge_labels=edge_labels)
        plt.show()

    def min_spanning_tree(self):
        weights_sum = 0
        edges = set()
        self.selected_vertices[self.start_vertex] = True
        while self.number_of_edges < self.number_of_vertices - 1:
            minimum = float("inf")
            x, y = 0, 0  # placeholders for 2 vertcies that make an edge
            for i in range(self.number_of_vertices):
                if self.selected_vertices[i]:
                    for j in range(self.number_of_vertices):
                        if not self.selected_vertices[j] and self.adj_matrix[i][j]:
                            if minimum > self.adj_matrix[i][j]:
                                minimum = self.adj_matrix[i][j]
                                x = i
                                y = j
            weight = self.adj_matrix[x][y]
            # edges.add(((x, y), weight))
            edges.add(frozenset((x, y)))
            weights_sum += weight
            self.selected_vertices[y] = True
            self.number_of_edges += 1

        return edges


def main(adj_matrix):
    if check_if_has_dfs_tree.dfs_tree(adj_matrix, 0):
        prim = Prim(adj_matrix, 0)
        return prim.min_spanning_tree()
    else:
        return "Graph is not connected"
