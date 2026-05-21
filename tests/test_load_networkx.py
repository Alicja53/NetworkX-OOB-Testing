import networkx as nx
import time
import os
import csv

def run_automated_suite():
    print("==================================================")
    print("URUCHAMIANIE REJESTRACJI TESTÓW WYDAJNOŚCIOWYCH")
    print("==================================================")
    
    edge_variants = [100000, 500000, 1000000]
    nodes = 5000
    results = []
    
    for edges in edge_variants:
        print(f"\nUruchamianie pomiaru dla M = {edges} krawędzi...")
        start_time = time.time()
        G = nx.gnm_random_graph(nodes, edges, seed=42)
        end_time = time.time()
        
        duration = end_time - start_time
        print(f"-> Zakończono w: {duration:.4f}s")
        
        # Zbieranie danych do pliku CSV
        results.append([edges, round(duration, 4)])
        del G
    
    # Wytyczna 2: Zapis danych do pliku tests/results.csv
    os.makedirs("tests", exist_ok=True)
    csv_file = "tests/results.csv"
    with open(csv_file, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["liczba_krawedzi", "czas_operacji_sekundy"])
        writer.writerows(results)
    print(f"\n[SUKCES] Dane pomyślnie zarejestrowane w pliku: {csv_file}")

if __name__ == "__main__":
    run_automated_suite()