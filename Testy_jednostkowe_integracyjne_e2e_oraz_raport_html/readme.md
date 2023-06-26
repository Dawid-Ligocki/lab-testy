# Projekt Zarządzanie Pracownikami

Ten projekt to system zarządzania pracownikami, napisany w języku Python. Pozwala dodawać, usuwać i zarządzać informacjami o pracownikach, a także wykonywać różne operacje na danych.

## Uruchamianie testów

Aby uruchomić testy, wykonaj następujące kroki:

1. Upewnij się, że masz zainstalowane wymagane biblioteki. Jeśli nie, możesz zainstalować je przy użyciu narzędzia pip: `pip install -r req.txt`

2. Przejdź do katalogu, w którym znajduje się projekt.

3. Uruchom testy, wpisując w terminalu komendę: `pytest`
   
Testy zostaną wykonane, a wyniki będą wyświetlane na ekranie.

## Generowanie raportu HTML z testów

Aby wygenerować raport HTML z wynikami testów, wykonaj następujące kroki:

1. Upewnij się, że masz zainstalowaną bibliotekę `pytest-html`. Jeśli nie, możesz ją zainstalować przy użyciu polecenia:
 `pip install pytest-html`

2. Przejdź do katalogu, w którym znajduje się projekt.

3. Uruchom polecenie pytest z opcją `--html`, aby wygenerować raport HTML: `pytest --html=raport.html`


Raport HTML o nazwie `raport.html` zostanie wygenerowany w bieżącym katalogu.

4. Otwórz plik `raport.html` w przeglądarce internetowej, aby zobaczyć wyniki testów w formie czytelnej graficznie.

## Struktura projektu

- `pracownik.py`: Definicja klasy Pracownik.
- `zarzadzanie_pracownikami.py`: Definicja klasy ZarzadzaniePracownikami.
- `test_zarzadzanie_pracownikami.py`: Testy jednostkowe i integracyjne dla projektu.
- `raport.html`: Wygenerowany raport HTML z wynikami testów.

## Autor

Dawid Ligocki






