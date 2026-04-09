import networkx as nx
import time
import sys

class LoadNode:
    """Węzeł zaprojektowany do obciążania pamięci RAM."""
    def __init__(self, id):
        self.id = id
        self.data_payload = "X" * 5120  # 5KB danych

    def __hash__(self): return hash(self.id)
    def __eq__(self, other): return self.id == other.id

def test_data_load_capacity():
    print("\n--- TEST 1: WYDAJNOŚĆ ZAPISU WĘZŁÓW ---")
    G = nx.Graph()
    start = time.time()
    for i in range(50000):
        G.add_node(LoadNode(i))
    end = time.time()
    print(f"Dodano 50k ciężkich węzłów w: {end-start:.4f}s")
    print(f"Rozmiar struktury G: {sys.getsizeof(G) / 1024:.2f} KB")

def test_edge_flooding():
    print("\n--- TEST 2: OBCIĄŻENIE RELACJI (EDGE FLOODING) ---")
    G = nx.Graph()
    nodes = [LoadNode(i) for i in range(10000)]
    G.add_nodes_from(nodes)
    
    start = time.time()
    for i in range(len(nodes) - 1):
        for j in range(1, 51):
            if i + j < len(nodes):
                G.add_edge(nodes[i], nodes[i+j])
    end = time.time()
    print(f"Wygenerowano {G.number_of_edges()} krawędzi w: {end-start:.4f}s")

if __name__ == "__main__":
    print("WYBÓR TESTU OBCIĄŻENIOWEGO:")
    print("1. Test węzłów (Memory Load)")
    print("2. Test krawędzi (Edge Flooding)")
    print("3. Wykonaj wszystkie (Memory Load + Edge Flooding)")
    
    wybor = input("Wybierz numer (1-3): ")
    
    if wybor == '1':
        test_data_load_capacity()
    elif wybor == '2':
        test_edge_flooding()
    elif wybor == '3':
        test_data_load_capacity()
        test_edge_flooding()
    else:
        print("Błędny wybór. Zamykanie.")