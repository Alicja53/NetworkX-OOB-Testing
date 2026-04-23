import networkx as nx

#sprawdzanie czy funkcje podają odpowiednie ilości granic i węzłów
def checking_number_of_entities(Graph):
    if Graph.number_of_nodes() != 10000:
        print("Zła ilość węzłów")
        return  False
    if Graph.number_of_edges() != 20000:
        print("złą ilość granic")
        return False
    return True


# tworzenie grafu
Graph = nx.DiGraph()

#dodawanie 10000 węzłów
for i in range(1,10001):
    Graph.add_node(i)

#dodawanie 20000 granic
for i in range(1,1001):
    for g in range(1,21):
        Graph.add_edge(i, i+g)
        
#wywołanie funkcji
print(checking_number_of_entities(Graph))