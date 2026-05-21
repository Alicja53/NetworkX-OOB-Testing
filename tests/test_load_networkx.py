import networkx as nx
import time
import os
import csv
import psutil

def get_memory_usage():
    # Pobiera zużycie pamięci RAM przez nasz skrypt w MB
    process = psutil.Process(os.getpid())
    return process.memory_info().rss / (1024 * 1024)

def run_automated_suite():
    print("==================================================")
    print("URUCHAMIANIE REJESTRACJI TESTÓW WYDAJNOŚCIOWYCH")
    print("==================================================")
    
    edge_variants = [100000, 500000, 1000000]
    nodes = 5000
    results = []
    
    for edges in edge_variants:
        print(f"\nUruchamianie pomiaru dla M = {edges} krawędzi...")
        
        # Pomiar pamięci przed generowaniem grafu
        ram_before = get_memory_usage()
        
        start_time = time.time()
        G = nx.gnm_random_graph(nodes, edges, seed=42)
        end_time = time.time()
        
        duration = end_time - start_time
        # Pomiar pamięci po wygenerowaniu grafu
        ram_after = get_memory_usage()
        ram_used = ram_after - ram_before
        
        print(f"-> Zakończono w: {duration:.4f}s")
        
        # Wytyczna 3: Monitoring zasobów dla największego grafu (1M)
        if edges == 1000000:
            print(f"-> [MONITORING ZASOBÓW] Zużycie RAM dla grafu 1M: {ram_used:.2f} MB")
        
        results.append([edges, round(duration, 4)])
        del G
    
    os.makedirs("tests", exist_ok=True)
    csv_file = "tests/results.csv"
    with open(csv_file, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["liczba_krawedzi", "czas_operacji_sekundy"])
        writer.writerows(results)
    print(f"\n[SUKCES] Dane pomyślnie zarejestrowane w pliku: {csv_file}")

if __name__ == "__main__":
    run_automated_suite()