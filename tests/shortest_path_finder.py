#import biblioteki do testowania(networkx)
import networkx as nx


# znajdowanie najkrótszych dróg za pomocą shortest_path
def finding_shortest_path(First_Graph, Second_Graph):
    # zapisywanie wyniku funkcji shortest_patch do zmiennych
    First = nx.shortest_path(First_Graph, 3, 6)
    Second = nx.shortest_path(Second_Graph, 3, 6, weight='weight')


    # sprawdzanie poprawności wyników funkcji
    if First != [3, 1, 6]:
        print("nie znaleziono najkrótszej drogi dla grafu bez atrybutu weight")
        return False
    if Second != [3, 4, 5, 6]:
        print("nie znaleziono najkrótszej drogi dla grafu z atrybutem weight")
        return False
    return True


#tworzenie pierwszego grafu testowego bez atrybutu weight
Edges1=[(1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (2, 3), (3, 4), (4, 5), (5, 6), (6,2)]
First_Graph = nx.Graph()
First_Graph.add_edges_from(Edges1)


#tworzenie drugiego grafu testowego z atrybutem weight
Second_Graph = nx.Graph()
Second_Graph.add_edge(1, 2, weight=3)
Second_Graph.add_edge(1, 3, weight=2)
Second_Graph.add_edge(1, 4, weight=3)
Second_Graph.add_edge(1, 5, weight=3)
Second_Graph.add_edge(1, 6, weight=2)
Second_Graph.add_edge(2, 3, weight=3)
Second_Graph.add_edge(3, 4, weight=1)
Second_Graph.add_edge(4, 5, weight=1)
Second_Graph.add_edge(5, 6, weight=1)
Second_Graph.add_edge(6, 2, weight=3)


#rysowanie obu grafów testowych z labelami
nx.draw(First_Graph, with_labels=True)
nx.draw(Second_Graph, with_labels=True)


print(finding_shortest_path(First_Graph, Second_Graph))



