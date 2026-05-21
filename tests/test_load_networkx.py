import networkx as nx
import time
import os
import csv
import resource

def get_memory_usage():
    usage = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    return usage / 1024

def test_run_automated_suite():
    print("==================================================")
    print("URUCHAMIANIE REJESTRACJI TESTÓW WYDAJNOŚCIOWYCH")
    print("==================================================")
    
    edge_variants = [100000, 500000, 1000000]
    nodes = 5000
    
    os.makedirs("tests", exist_ok=True)
    csv_file = "tests/results.csv"
    
    if os.path.exists(csv_file):
        os.remove(csv_file)
        
    with open(csv_file, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file, delimiter=";")
        writer.writerow(["Liczba_krawedzi", "Czas_operacji_sekundy"])
    
    for edges in edge_variants:
        print(f"Uruchamianie pomiaru dla M = {edges} krawędzi...")
        
        ram_before = get_memory_usage()
        start_time = time.time()
        
        G = nx.gnm_random_graph(nodes, edges, seed=42)
        
        end_time = time.time()
        ram_after = get_memory_usage()
        duration = end_time - start_time
        ram_used = ram_after - ram_before
        
        print(f"-> Zakończono w: {duration:.4f}s")
        if edges == 1000000:
            print(f"-> Zużycie RAM dla 1M: {ram_used:.2f} MB")
        
        with open(csv_file, mode="a", newline="", encoding="utf-8") as file:
            writer = csv.writer(file, delimiter=";")
            writer.writerow([edges, round(duration, 4)])
            
        del G

    assert os.path.exists(csv_file) is True