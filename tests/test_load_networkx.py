import networkx as nx
import time
import sys

class LoadNode:
    """Węzeł zaprojektowany do obciążania pamięci RAM."""
    def __init__(self, id):
        self.id = id
        # Każdy węzeł niesie ze sobą 5KB 'śmieciowych' danych
        self.data_payload = "X" * 5120 

    def __hash__(self): return hash(self.id)
    def __eq__(self, other): return self.id == other.id

def test_data_load_capacity():
    print("\n--- TEST: WYDAJNOŚĆ ZAPISU WŁASNYCH WĘZŁÓW ---")
    G = nx.Graph()
    start = time.time()
    
    # Próba masowego zapisu 50 000 ciężkich węzłów
    for i in range(50000):
        G.add_node(LoadNode(i))
        
    end = time.time()
    print(f"Dodano 50k ciężkich węzłów w czasie: {end-start:.4f}s")
    print(f"Przybliżony rozmiar grafu w RAM: {sys.getsizeof(G) / 1024:.2f} KB")

if __name__ == "__main__":
    test_data_load_capacity()