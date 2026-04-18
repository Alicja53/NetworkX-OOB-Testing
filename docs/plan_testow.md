# Rozszerzony Plan Testów: Moduł NetworkX (OOB)

## 1. Cel dokumentacji
Niniejszy plan opisuje szczegółowe kroki weryfikacji biblioteki **NetworkX**. Celem jest sprawdzenie, czy moduł po instalacji zachowuje się przewidywalnie, nie gubi danych i radzi sobie z dużymi obciążeniami.

---

## 2. Testy Funkcjonalne (Poprawność Logiki)
Te testy mają potwierdzić, że podstawowe mechanizmy biblioteki działają zgodnie z matematycznymi założeniami.

### Scenariusz F1: Integralność struktury grafu
* **Opis:** Tworzymy pusty graf skierowany (`DiGraph`) i dodajemy do niego pętlą dokładnie **10 000 węzłów** oraz **20 000 losowych krawędzi**.
* **Weryfikacja:** Wywołujemy funkcje `number_of_nodes()` oraz `number_of_edges()`.
* **Oczekiwany wynik:** Liczba elementów wewnątrz obiektu musi być identyczna z liczbą danych wprowadzonych. Każda rozbieżność oznacza błąd w zarządzaniu pamięcią grafu.

### Scenariusz F2: Test najkrótszej ścieżki (Dijkstra)
* **Opis:** Budujemy graf o znanej strukturze (np. siatka lub pierścień), gdzie odległość między dwoma punktami jest nam znana przed uruchomieniem programu.
* **Weryfikacja:** Uruchamiamy funkcję `shortest_path` i porównujemy wynik z naszymi obliczeniami "na papierze".
* **Oczekiwany wynik:** Algorytm musi zwrócić najkrótszą możliwą drogę. Test kończy się niepowodzeniem, jeśli znaleziona trasa jest dłuższa lub nie istnieje.

---

## 3. Testy Wydajnościowe (Skala i Szybkość)
Celem jest wyznaczenie granic możliwości biblioteki i sprawdzenie, jak czas operacji rośnie wraz z ilością danych.

### Scenariusz W1: Test obciążeniowy (Stress Test)
* **Opis:** Generujemy grafy losowe o trzech różnych skalach:
  1. **Mała:** 100 000 krawędzi.
  2. **Średnia:** 500 000 krawędzi.
  3. **Duża:** 1 000 000 krawędzi.
* **Weryfikacja:** Mierzony jest czas (w sekundach) potrzebny na pełne wygenerowanie grafu oraz czas wykonania prostego algorytmu (np. wyliczenie stopnia centralności).
* **Oczekiwany wynik:** Czas operacji powinien rosnąć liniowo lub logarytmicznie. Gwałtowny, wykładniczy wzrost czasu przy skali 1M oznacza niską wydajność modułu w zadaniach Big Data.

---

## 4. Metodyka wykonania (Instrukcja dla programistów)
Aby zachować spójność w projekcie, przyjmujemy następujące zasady techniczne:

1. **Automatyzacja:** Wszystkie testy funkcjonalne (F1, F2) muszą być napisane w formie asercji (`assert`). Jeśli wynik jest zły, skrypt ma przerwać działanie i zgłosić błąd.
2. **Logowanie wyników:** Testy wydajnościowe (W1) powinny zapisywać czasy operacji do pliku `results.csv` w folderze `/tests`, aby umożliwić późniejszą analizę.
3. **Środowisko:** Testy muszą uruchamiać się na czystej instalacji biblioteki pobranej komendą `pip install networkx`.
