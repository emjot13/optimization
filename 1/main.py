import directed
import undirected

def main():
    while True:
        try:
            amount = int(input("Enter number of nodes to initialize a graph\n"))
            break
        except ValueError:
            continue


    while True:
        graph_type = input("Enter `d` for directed graph and `u' for undericted\n")
        if graph_type == "d":
            directed.Directed_Graph(amount)
            break
        if graph_type == "u":
            undirected.Undirected_Graph(amount)
            break



if __name__ == main():
    main()




