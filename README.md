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

| Etap | Termin | Zadania i Cele | Rezultat (Milestone) |
| :--- | :--- | :--- | :--- |
| **Etap 1** | **do 17.04.2026** | **Organizacja:** Inicjalizacja repozytorium, dokumentacja startowa, wybór modułu PyPI i podział ról. | Repozytorium gotowe do oceny (START) |
| **Etap 2** | **do 24.04.2026** | **Zarządzanie:** Konfiguracja Issues i Pull Requestów. Wdrożenie szkieletów testów funkcjonalnych. | Aktywny workflow i zarządzanie kodem |
| **Etap 3** | **do 08.05.2026** | **Automatyzacja:** Pełna implementacja testów wydajnościowych. Konfiguracja manualnej Pipeline. | Działający system CI/CD |
| **Etap 4** | **do 22.05.2026** | **Release:** Raport końcowy, samoocena zespołu i oficjalne zamknięcie projektu. | Stabilna wersja końcowa (RELEASE) |

---

## 4. Komunikacja i zasady współpracy

W celu zapewnienia sprawnej realizacji projektu oraz wysokiej jakości kodu, zespół przyjął następujące zasady:

* **Kanały komunikacji:** * **Messenger:** Bieżąca komunikacja operacyjna i szybkie ustalenia.
  * **Discord:** Cotygodniowe spotkania statusowe (środy po lekcjach) oraz wspólne sesje rozwiązywania problemów technicznych.
* **Zarządzanie zadaniami:** Wszystkie prace są rejestrowane w zakładce **GitHub Issues**. Każde zadanie musi mieć przypisanego wykonawcę (Assignee).
* **Zasady pracy z kodem (Workflow):**
  * Obowiązuje zakaz bezpośredniego wypychania kodu (push) do gałęzi `main`.
  * Każda funkcjonalność/test powstaje na osobnym branchu.
  * Połączenie kodu z główną gałęzią odbywa się wyłącznie poprzez **Pull Request** po uprzednim sprawdzeniu przez leadera zespołu.
* **Dokumentacja:** Każda zmiana w kodzie wymagająca wyjaśnienia musi zostać udokumentowana w odpowiednim pliku w folderze `/docs`.

---

## 5. Plan testów
Na obecnym etapie zakładamy weryfikację biblioteki w trzech kluczowych obszarach:
* **Integracja danych**: Sprawdzenie poprawności zapisu węzłów i relacji w strukturze grafu, aby wyeliminować ryzyko utraty danych podczas budowy sieci.
* **Weryfikacja algorytmów**: Testowanie poprawności wyników zwracanych przez kluczowe algorytmy ścieżkowe w odniesieniu do założeń matematycznych.
* **Analiza wydajnościowa**: Pomiary czasu wykonania operacji pod obciążeniem, mające na celu określenie limitów stabilności biblioteki dla dużych zbiorów danych.

## 6. Instrukcja uruchomienia (Quick Start)

System testowania został przygotowany do uruchomienia w dwóch trybach: lokalnym (do prac deweloperskich) oraz zdalnym (weryfikacja końcowa).

### Tryb lokalny (Lokalne środowisko Python)
Wymagany Python 3.10+ oraz menedżer pakietów `pip`.

| Krok | Operacja | Komenda |
| :--- | :--- | :--- |
| **1** | Pobranie repozytorium | `git clone https://github.com/Alicja53/NetworkX-OOB-Testing.git` |
| **2** | Instalacja bibliotek | `pip install -r requirements.txt` |
| **3** | Testy funkcjonalne | `pytest tests/test_logic.py` |
| **4** | Testy wydajnościowe | `python tests/test_performance.py` |

### Tryb zdalny (GitHub Actions)
Zautomatyzowana weryfikacja OOB na zewnętrznej infrastrukturze.

1.  Przejdź do sekcji **Actions** w menu górnym repozytorium.
2.  Z listy po lewej stronie wybierz workflow: **NetworkX OOB Testing**.
3.  Użyj selektora **Run workflow** -> **Branch: main** -> potwierdź uruchomienie.
4.  Szczegółowe logi z wykonania testów (wyniki `pytest` oraz czasy wydajnościowe) dostępne są w podglądzie zadania po jego zakończeniu.
