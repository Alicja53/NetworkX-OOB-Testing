# Raport Końcowy z Testów OOB: Biblioteka NetworkX
**Status projektu:** RELEASE (Wersja finalna)

---

## 1. Cel projektu i podejście OOB
Projekt zrealizował pełną weryfikację stabilności, poprawności algorytmicznej oraz wydajności biblioteki **NetworkX** pobranej bezpośrednio z repozytorium PyPI. Testy zostały przeprowadzone w formule **Out-Of-The-Box (OOB)**. Oznacza to badanie zachowania czystej biblioteki w odizolowanym środowisku, bezpośrednio po instalacji menedżerem pakietów, bez wprowadzania jakichkolwiek modyfikacji w jej kodzie źródłowym.

## 2. Automatyzacja procesów i unifikacja potoku (CI/CD)
Proces weryfikacji został w pełni zautomatyzowany za pomocą platformy **GitHub Actions** (`python-app.yml`). Ze względu na specyfikację testów OOB, potok uruchamiany jest manualnie przez administratora (`workflow_dispatch`).

W końcowej fazie projektu potok został skonfigurowany do automatycznego skanowania całego katalogu za pomocą komendy `pytest tests/ -o python_files="*.py"`. Dzięki temu rozwiązaniu framework Pytest wymusza wykonanie każdego pliku testowego znajdującego się w folderze, eliminując ryzyko pominięcia jakiegokolwiek modułu ze względu na domyślne konwencje nazewnictwa.

**Przebieg potoku w chmurze (Status: Success):**
1. Inicjalizacja czystego, odizolowanego środowiska `ubuntu-latest` z Pythonem 3.10.
2. Automatyczna instalacja oficjalnej biblioteki `networkx` oraz frameworku `pytest`.
3. Wykonanie zunifikowanego kroku testów funkcjonalnych i automatyczna agregacja wyników do jednego pliku raportu `--junitxml=report.xml`.
4. Uruchomienie skryptu obciążeniowego `test_load_networkx.py` badającego skalowalność biblioteki.
5. Archiwizacja oraz wystawienie raportu XML oraz tabeli wynikowej `tests/results.csv` jako oficjalnych, pobieralnych artefaktów końcowych potoku (`test-results`).

## 3. Zbiorcza Analiza Wyników Testów
* **Testy funkcjonalne i poprawnościowe:** Zweryfikowano działanie algorytmów wyszukiwania najkrótszych ścieżek (Dijkstra) dla grafów ważonych i nieważonych. Za pomocą dedykowanych testów sprawdzono również zachowanie biblioteki w warunkach skrajnych (testy negatywne, np. próba szukania ścieżki w grafie bez połączeń). Biblioteka poprawnie generuje wyjątki `NetworkXNoPath` oraz `NodeNotFound`, co potwierdza heretycką stabilność i odporność na błędy logiczne użytkownika.
* **Testy wydajnościowe (Skalowanie):** Pomiary automatyczne zarejestrowane w pliku `results.csv` dla wielkości obciążenia 100k, 500k oraz 1M krawędzi wykazały stabilny, liniowy wzrost czasu obliczeń (maksymalnie do 2.81s dla skali 1 000 000 krawędzi). Udowadnia to optymalną złożoność obliczeniową struktur wewnętrznych NetworkX i pełną gotowość do pracy pod dużym obciążeniem.

## 4. Wykaz zrealizowanych prac i podział obowiązków
Poniższe zestawienie przedstawia faktyczny podział zadań inżynierskich i dokumentacyjnych w zespole, udokumentowany bezpośrednio w statystykach oraz historii repozytorium:

* **Alicja (Alicja53) – Koordynator Projektu / DevOps:**
  * Utworzenie i zarządzanie strukturą repozytorium.
  * Przygotowanie i pełna konfiguracja potoku CI/CD w pliku `.github/workflows/python-app.yml`.
  * Wdrożenie flagi unifikacyjnej `-o python_files="*.py"` zapewniającej pełne pokrycie testowe katalogu przez framework Pytest.
  * Skonfigurowanie automatycznego generowania raportu JUnit XML oraz zbierania artefaktów.
  * Opracowanie i aktualizacja struktury dokumentacji projektowej (`README.md`, `docs/plan_testow.md`, `docs/raport_koncowy.md`).

* **Grzegorz (GDabrowsk) – Tester Funkcjonalny:**
  * Implementacja testów weryfikujących poprawność logiczną wyznaczania ścieżek algorytmem Dijkstry w pliku `tests/shortest_path_finder.py`.
  * Przygotowanie skryptu weryfikacji struktury grafu w pliku `tests/graph_integrity_test.py`.
  * Opracowanie scenariusza obsługi błędów i testów negatywnych w pliku `tests/Test_meant_to_fail.py`.

* **Karol (MATRIii) – Tester Wydajnościowy:**
  * Opracowanie i implementacja skryptu do generowania losowych struktur grafowych oraz pomiaru czasu operacji pod obciążeniem do 1M krawędzi w pliku `tests/test_load_networkx.py`.
  * Przygotowanie bazowej struktury pliku `tests/results.csv` służącego jako docelowy szablon zapisu danych pomiarowych w potoku CI/CD.

## 5. Podsumowanie i Werdykt
Biblioteka NetworkX w pełni pomyślnie przeszła procedurę testową Out-Of-The-Box. Produkt wykazuje wysokie standardy optymalizacji, odporności na błędy oraz stabilności instalacyjnej. Moduł jest w pełni rekomendowany do wdrożeń produkcyjnych.
