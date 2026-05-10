# Scenariusze Testów Akceptacyjnych (UAT)

Poniższa tabela definiuje kryteria akceptacji projektu "NetworkX OOB Testing". Scenariusze te służą do ostatecznej weryfikacji, czy system spełnia założenia testowania Out-Of-The-Box.

| ID | Scenariusz | Procedura testowa | Oczekiwany wynik (Kryterium sukcesu) |
| :--- | :--- | :--- | :--- |
| **UAT-01** | **Instalacja OOB** | Sklonowanie repozytorium i wykonanie `pip install -r requirements.txt`. | Wszystkie zależności (NetworkX, Pytest) instalują się bez błędów. |
| **UAT-02** | **Weryfikacja algorytmów** | Uruchomienie testów funkcjonalnych komendą `pytest tests/test_logic.py`. | Wszystkie asercje algorytmiczne (np. najkrótsza ścieżka) zwracają status "Passed". |
| **UAT-03** | **Stabilność wydajności** | Uruchomienie skryptu `tests/test_performance.py`. | System wykonuje pomiary dla grafów o dużej skali bez błędów pamięci i generuje logi czasowe. |
| **UAT-04** | **Zdalna automatyzacja** | Manualne wyzwalanie akcji w zakładce "Actions" na platformie GitHub. | Pipeline przechodzi przez wszystkie etapy i kończy się statusem "Success" (zielony znacznik). |
| **UAT-05** | **Integralność docs** | Przegląd zgodności dokumentacji z aktualną strukturą katalogów. | Dokumentacja w `/docs` odzwierciedla faktyczny stan testów w `/tests`. |

---
