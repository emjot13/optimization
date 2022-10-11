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
        from_file = input("Do you want to load graph from a file [y/n] ")
        if from_file in ["y", "n"]:
            from_file = True if from_file == "y" else False
            break

    while True:
        graph_type = input("Enter `d` for directed graph and `u' for undericted\n")
        if graph_type == "d":
            directed.Directed_Graph(amount)
            break
        if graph_type == "u":
            undirected.Undirected_Graph(amount, from_file)
            break



if __name__ == main():
    main()




