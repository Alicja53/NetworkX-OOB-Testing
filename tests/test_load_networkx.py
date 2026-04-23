import networkx as nx
import time

def test_graph_performance():
    print("\n--- TEST 1: GENEROWANIE GRAFU (100K KRAWDZI) ---")
    
    # Parametry: n - węzły, m - krawędzie
    n = 5000 
    m = 1000000 
    
    start = time.time()
    # Generowanie grafu o zadanej liczbie krawędzi
    G = nx.gnm_random_graph(n, m)
    end = time.time()
    
    print(f"Wygenerowano graf ({m} krawędzi) w: {end-start:.4f}s")

if __name__ == "__main__":
    print("WYBÓR TESTU OBCIĄŻENIOWEGO:")
    print("1. Scenariusz W1 (100k krawędzi)")
    
    wybor = input("Wybierz numer: ")
    
    if wybor == '1':
        test_graph_performance()
    else:
        print("Błędny wybór. Zamykanie.")