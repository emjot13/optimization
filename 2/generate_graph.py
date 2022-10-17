from itertools import combinations, groupby
import networkx as nx
import random
import matplotlib.pyplot as plt


def gnp_random_connected_graph(n, p):
    """
    Generates a random undirected graph, similarly to an Erdős-Rényi 
    graph, but enforcing that the resulting graph is conneted
    """
    edges = combinations(range(n), 2)
    G = nx.Graph()
    G.add_nodes_from(range(n))
    if p <= 0:
        return G
    if p >= 1:
        return nx.complete_graph(n, create_using=G)
    for _, node_edges in groupby(edges, key=lambda x: x[0]):
        node_edges = list(node_edges)
        random_edge = random.choice(node_edges)
        G.add_edge(*random_edge)
        for e in node_edges:
            if random.random() < p:
                G.add_edge(*e)
    return G



nodes = 1000
seed = random.randint(1,10)
probability = 0.1
G = gnp_random_connected_graph(nodes,probability)


matrix = nx.adjacency_matrix(G)
m = nx.to_numpy_array(G)

with open("graph2.txt", "w") as f:
    for line in m:
        # print(line)
        f.write(", ".join([str(int(x)) for x in line]) + "\n")

# print(list(m))

# plt.figure(figsize=(8,5))
# nx.draw(G, node_color='lightblue', 
#         with_labels=True, 
#         node_size=500)



# plt.show()