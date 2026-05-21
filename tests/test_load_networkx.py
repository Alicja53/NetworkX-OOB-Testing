import networkx as nx
import time

def run_automated_suite():
    print("==================================================")
    print("URUCHAMIANIE REJESTRACJI TESTÓW WYDAJNOŚCIOWYCH")
    print("==================================================")
    
    edge_variants = [100000, 500000, 1000000]
    nodes = 5000
    
    for edges in edge_variants:
        print(f"\nUruchamianie pomiaru dla M = {edges} krawędzi...")
        start_time = time.time()
        G = nx.gnm_random_graph(nodes, edges, seed=42)
        end_time = time.time()
        print(f"-> Zakończono w: {end_time - start_time:.4f}s")
        del G

if __name__ == "__main__":
    run_automated_suite()