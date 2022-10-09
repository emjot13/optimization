import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import random as rd

class Directed_Graph:
    def __init__(self, number_of_nodes) -> None:
        self.adjacency_matrix = [[0] * number_of_nodes for _ in range(number_of_nodes)]
        self.non = number_of_nodes
        self.actions = {
        1: self.show_graph,
        2: self.add_vertex,
        3: self.remove_vertex,
        4: self.add_edge,
        5: self.remove_edge,
        6: self.vertex_deegre,
        7: self.min_max,
        8: self.odd_even,
        9: self.sort_vertices,
        10: exit
    }

        self.show_graph()
        self.choices()

    def validate_vertices(self, *args):
        for vertex in args:
            if not 0 <= vertex <= self.non - 1:
                return False
        return True


    def choices(self):
        while True:
            action = input("""
1. Show graph
2. Add vertex
3. Remove vertex
4. Add edge
5. Remove edge
6. Vertex degree
7. Min and max graph degree
8. Odd and even
9. Sorted
10. Exit
""")        
            if action in [str(x) for x in range(1, 11)]:
                self.actions[int(action)]()

            


    def show_graph(self):
        colors = [tuple(rd.random() for _ in range(3)) for _ in range(self.non)]
        self.labels = {_: _ for _ in range(self.non)}
        adc_matrix = np.matrix(self.adjacency_matrix)
        graph=nx.from_numpy_matrix(adc_matrix, create_using=nx.MultiDiGraph())
        nx.draw(graph, arrows=True, node_color=colors, with_labels=True, labels=self.labels, connectionstyle='arc3, rad = 0.1')
        plt.show()


    def add_vertex(self):
        self.non += 1
        for item in self.adjacency_matrix:
            item.append(0)
        self.adjacency_matrix.append([0] * self.non)
        print(f"Added vertex number {self.non - 1}")
    
    def remove_vertex(self):
        while True:
            try:
                vertex_to_delete = int(input("Enter the vertex to remove "))
            except ValueError:
                print("Must be integer")
                continue
            if self.validate_vertices(vertex_to_delete):
                del self.adjacency_matrix[vertex_to_delete]
                for item in self.adjacency_matrix:
                    del item[vertex_to_delete]
                self.non -= 1
                break
            else:
                print("Incorrect vertex")
                print("Possible vertices:")
                for vertex in range(self.non):
                    print(vertex)
    
    def add_edge(self):
        while True:
            try:
                vertex1 = int(input("Enter the vertex from which edge starts "))
                vertex2 = int(input("Enter the vertex to which edge goes "))
            except ValueError:
                print("Vertices must be integers")
                continue

            if self.validate_vertices(vertex1, vertex2):
                self.adjacency_matrix[vertex1][vertex2] += 1
                break
            else:
                print("Incorrect vertices")
    

    def remove_edge(self):
        while True:
            try:
                vertex1 = int(input("Enter the vertex from which edge starts "))
                vertex2 = int(input("Enter the vertex to which edge goes "))
            except ValueError:
                continue


            if self.validate_vertices(vertex1, vertex2):
                if self.adjacency_matrix[vertex1][vertex2] > 0:
                    self.adjacency_matrix[vertex1][vertex2] -= 1
                    break
                else:
                    print("There is no edge between these nodes")
            else:
                print("Incorrect vertices")

    def vertex_deegre(self):
        while True:
            try:
                vertex = int(input("Enter the vertex"))
            except ValueError:
                print("Must be integer")

            if self.validate_vertices(vertex):
                negative, positive = self.get_deegres(vertex) #leaving, entering
                print(f"negative: {negative}, positive: {positive}")
            else:
                print("Incorrect vertices")

    

    def get_deegres(self, vertex):
        negative = sum(self.adjacency_matrix[vertex])
        positive = 0 # entering
        for l in self.adjacency_matrix:
            positive += l[vertex]
        return negative, positive
        
        
    
    def get_all_degrees(self):
        degrees = {}
        for node in range(len(self.adjacency_matrix)):
            n, p = self.get_deegres(node)
            degrees[node] = [n, p, n + p]
        return degrees
    
    def sort_vertices(self, verbose = True):
        degrees = self.get_all_degrees()
        degrees = sorted(degrees.items(), key=lambda x: -x[1][2])
        if verbose:
            for node, deg in degrees:
                print(f"node: {node}, negative: {deg[0]}, positive: {deg[1]}, total: {deg[2]}")
        return degrees

    def min_max(self):
        degrees = self.sort_vertices(False)
        print(f"max: {degrees[0]}, min: {degrees[-1]}")

    def odd_even(self):
        deegres = self.get_all_degrees()
        odd, even = 0, 0
        for v in deegres.values():
            if v[2] % 2 == 0:
                even += 1
            else:
                odd += 1
        print(f"Even: {even}, odd: {odd}")