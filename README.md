# System Testowania: NetworkX (OOB)

## 1. Opis projektu i plan działań
Projekt polega na automatycznej weryfikacji biblioteki NetworkX. Sprawdzamy, czy moduł po pobraniu z oficjalnego repozytorium PyPI działa poprawnie, stabilnie i wydajnie w standardowym środowisku pracy.

**Główne cele:**
* **Weryfikacja funkcjonalności:** Sprawdzenie, czy kluczowe algorytmy grafowe zwracają poprawne wyniki.
* **Testy wydajności:** Pomiar czasu operacji przy pracy na dużych zbiorach danych.
* **Automatyzacja:** Konfiguracja systemu, który automatycznie sprawdzi, czy biblioteka działa bez błędów.

---

## 2. Podział odpowiedzialności w zespole

### Koordynator Projektu (Alicja)
* **Organizacja:** Nadzór nad strukturą repozytorium oraz weryfikacja techniczna kodu.
* **Automatyzacja:** Konfiguracja mechanizmu, który automatycznie uruchamia testy na GitHubie.
* **Dokumentacja:** Opracowanie scenariuszy testowych oraz przygotowanie końcowych raportów.

### Tester Funkcjonalny (Grzegorz) - GDabrowsk 
* **Logika testów:** Przygotowanie skryptów weryfikujących poprawność działania funkcji biblioteki NetworkX.
* **Obsługa błędów:** Identyfikacja i dokumentowanie wszelkich nieprawidłowości w działaniu modułu poprzez system zadań w repozytorium.

### Tester Wydajnościowy (Karol) - MATRIii
* **Analiza wydajności:** Implementacja testów obciążeniowych mierzących czasy wykonywania operacji przy dużej liczbie węzłów i krawędzi.
* **Raportowanie:** Tworzenie czytelnych zestawień pomiarowych, które posłużą do oceny efektywności biblioteki.

---

## 3. Harmonogram prac
* **Etap 1:** Ustawienie repozytorium, dokumentacja startowa, definicja ról i scenariuszy testowych.
* **Etap 2:** Pisanie kodu testowego, wrzucanie go do repozytorium przez Pull Requesty i poprawianie błędów.
* **Etap 3:** Uruchomienie automatycznych testów, analiza wyników i przygotowanie finalnej prezentacji.

---

## 4. Komunikacja
* **Messenger:** Szybkie pytania i bieżące ustalenia.
* **Discord:** Wspólne sesje kodowania i rozwiązywanie problemów technicznych.
* **GitHub Issues:** Rejestrowanie wszystkich zadań i błędów, aby zachować porządek w pracy.

---

## 5. Plan testów
Na obecnym etapie zakładamy weryfikację biblioteki w trzech kluczowych obszarach:
* **Integracja danych**: Sprawdzenie poprawności zapisu węzłów i relacji w strukturze grafu, aby wyeliminować ryzyko utraty danych podczas budowy sieci.
* **Weryfikacja algorytmów**: Testowanie poprawności wyników zwracanych przez kluczowe algorytmy ścieżkowe w odniesieniu do założeń matematycznych.
* **Analiza wydajnościowa**: Pomiary czasu wykonania operacji pod obciążeniem, mające na celu określenie limitów stabilności biblioteki dla dużych zbiorów danych.
