#import biblioteki do testowania(networkx)
import networkx as nx
import pytest

def no_conection(Graph):
    # zapisywanie wyniku funkcji shortest_patch do zmiennych
    try:
        nx.shortest_path(Graph, 3, 8)
        # sprawdzanie poprawności wyników funkcji
        print("znaleziono najkrótszą drogę pomimo braku połączenia")
        return False
    except:
        return True


def no_edge(Graph):
    try:
        nx.shortest_path(Graph, 3, 80)

        # sprawdzanie poprawności wyników funkcji
        print("znaleziono najkrótszą drogę pomimo braku takiego elementu")
        return False
    except:
        return True


def no_graph(Graph):
    try:
        nx.average_clustering(Graph)

        # sprawdzanie poprawności wyników funkcji
        print("wykon ano operację pomimo pustego grafu")
        return False
    except:
        return True


#tworzenie pierwszego grafu testowego
Edges1=[(1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (2, 3), (3, 4), (4, 5), (5, 6), (6,2),(8,7)]
First_Graph = nx.Graph()
First_Graph.add_edges_from(Edges1)

#tworzenie drugiego pustego grafu testowego
Second_Graph = nx.Graph()

# Funkcja testowa dla pytest (konieczna do automatyzacji w GitHub Actions)
def test_failing_tests():
    assert no_conection(First_Graph) and no_edge(First_Graph) and no_graph(Second_Graph)



