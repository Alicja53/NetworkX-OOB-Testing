import networkx as nx
import time
import os
import csv
import resource
import gc


def get_memory_usage():
    """

    """
    usage = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    return usage / 1024


def run_performance_suite():

    print("==================================================")
    print("URUCHAMIANIE TESTÓW WYDAJNOŚCIOWYCH (MATRIii)")
    print("==================================================")

    edge_variants = [100000, 250000, 500000]

    nodes = 5000

    os.makedirs("tests", exist_ok=True)

    csv_file = "tests/results.csv"

    if os.path.exists(csv_file):
        os.remove(csv_file)

    with open(csv_file, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file, delimiter=";")

        writer.writerow([
            "Edges",
            "Time_s",
            "RAM_MB"
        ])

    for edges in edge_variants:

        print("\n===================================")
        print(f"START TESTU: {edges} krawędzi")
        print("===================================")

        try:

            ram_before = get_memory_usage()

            start_time = time.perf_counter()

            G = nx.gnm_random_graph(
                nodes,
                edges,
                seed=42
            )

            end_time = time.perf_counter()

            duration = end_time - start_time

            ram_after = get_memory_usage()

            ram_used = ram_after - ram_before

            print(f"[OK] Czas wykonania: {duration:.4f} s")
            print(f"[OK] Zużycie RAM: {ram_used:.2f} MB")


            with open(csv_file, mode="a", newline="", encoding="utf-8") as file:

                writer = csv.writer(
                    file,
                    delimiter=";"
                )

                writer.writerow([
                    edges,
                    round(duration, 4),
                    round(ram_used, 2)
                ])

            print(f"[DONE] Wynik zapisany dla {edges}")


            del G
            gc.collect()

        except MemoryError:

            print(f"[ERROR] MEMORY ERROR dla {edges}")

            with open(csv_file, mode="a", newline="", encoding="utf-8") as file:

                writer = csv.writer(
                    file,
                    delimiter=";"
                )

                writer.writerow([
                    edges,
                    "MEMORY_ERROR",
                    "N/A"
                ])

        except Exception as e:

            print(f"[ERROR] Nieznany błąd dla {edges}")
            print(str(e))

            with open(csv_file, mode="a", newline="", encoding="utf-8") as file:

                writer = csv.writer(
                    file,
                    delimiter=";"
                )

                writer.writerow([
                    edges,
                    "ERROR",
                    str(e)
                ])

    print("\n==================================================")
    print("[SUKCES] Wszystkie testy zakończone")
    print(f"Wyniki zapisano do: {csv_file}")
    print("==================================================")

    assert os.path.exists(csv_file)


if __name__ == "__main__":
    run_performance_suite()