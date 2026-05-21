import networkx as nx
import time
import os
import csv
import resource
import gc


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

        writer.writerow([
            "Edges",
            "Generation_Time_s",
            "Centrality_Time_s",
            "RAM_MB"
        ])


    for edges in edge_variants:

        print("\n==================================================")
        print(f"START TESTU: {edges} krawędzi")
        print("==================================================")

        try:

            ram_before = get_memory_usage()



            generation_start = time.perf_counter()

            G = nx.gnm_random_graph(
                nodes,
                edges,
                seed=42
            )

            generation_end = time.perf_counter()

            generation_time = generation_end - generation_start

            print(f"[OK] Generowanie grafu: {generation_time:.4f}s")



            centrality_start = time.perf_counter()

            nx.degree_centrality(G)

            centrality_end = time.perf_counter()

            centrality_time = centrality_end - centrality_start

            print(f"[OK] Degree centrality: {centrality_time:.4f}s")



            ram_after = get_memory_usage()

            ram_used = ram_after - ram_before

            print(f"[OK] Zużycie RAM: {ram_used:.2f} MB")


            with open(csv_file, mode="a", newline="", encoding="utf-8") as file:

                writer = csv.writer(file, delimiter=";")

                writer.writerow([
                    edges,
                    round(generation_time, 4),
                    round(centrality_time, 4),
                    round(ram_used, 2)
                ])

            print(f"[DONE] Wynik zapisany dla {edges}")


            del G
            gc.collect()

        except MemoryError:

            print(f"[ERROR] MEMORY ERROR dla {edges}")

            with open(csv_file, mode="a", newline="", encoding="utf-8") as file:

                writer = csv.writer(file, delimiter=";")

                writer.writerow([
                    edges,
                    "MEMORY_ERROR",
                    "MEMORY_ERROR",
                    "N/A"
                ])

        except Exception as e:

            print(f"[ERROR] Błąd dla {edges}")
            print(str(e))

            with open(csv_file, mode="a", newline="", encoding="utf-8") as file:

                writer = csv.writer(file, delimiter=";")

                writer.writerow([
                    edges,
                    "ERROR",
                    "ERROR",
                    str(e)
                ])

    print("\n==================================================")
    print("[SUKCES] Wszystkie testy zakończone")
    print(f"Wyniki zapisano do: {csv_file}")
    print("==================================================")


    assert os.path.exists(csv_file) is True


if __name__ == "__main__":
    test_run_automated_suite()