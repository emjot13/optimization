class Stack:
    def __init__(self):
        self.list = []

    def print_stack(self):
        return self.list

    def push(self, item):
        self.list.append(item)

    def pop(self):
        return self.list.pop()

    def top(self):
        return self.list[-1]

    def is_empty(self):
        return len(self.list) == 0


def dfs_tree(graph, start):
    edges = set()
    nodes_number = len(graph)
    visited = [False] * nodes_number
    stack = Stack()
    stack.push(start)
    visited[start] = True
    while not stack.is_empty():
        # print([x + 1 for x in stack.print_stack()]) 
        vertex = stack.top()
        for i in range(len(graph[vertex])):
            if graph[vertex][i] and not visited[i]:
                stack.push(i)
                visited[i] = True
                edges.add((vertex + 1, i + 1))
                break
        else:
            stack.pop()
    return edges if all(visited) else False



def main():
    import networkx as nx
    import numpy as np
    import matplotlib.pyplot as plt

    graph = [
        [0, 1, 1, 0, 0], 
        [1, 0, 0, 0, 1],
        [1, 1, 0, 1, 1],
        [0, 0, 1, 0, 0],
        [0, 1, 1, 0, 0]
    ]
    as_np = np.matrix(graph)
    nx_graph = nx.from_numpy_matrix(as_np)

    nx.draw(nx_graph, with_labels=True, labels = {x: x + 1 for x in range(len(graph))})
    tree = dfs_tree(graph, 2)
    print(tree)
    plt.show()
    spanning_tree = nx.Graph()
    spanning_tree.add_nodes_from([x for x in range(len(graph))])
    for pair in tree:
        spanning_tree.add_edge(pair[0] - 1, pair[1] - 1)

    nx.draw(spanning_tree, with_labels = True, labels = {x: x + 1 for x in range(len(graph))})
    plt.show()



if __name__ == '__main__':
    main()
