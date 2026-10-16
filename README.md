# keepass-dict-atack

Prosty skrypt do **odzyskiwania dostępu do własnej bazy KeePass** metodą słownikową.

## Ważne: użycie legalne i etyczne

To narzędzie jest udostępnione **wyłącznie** do:
- odzyskiwania hasła do bazy, której jesteś właścicielem,
- testów bezpieczeństwa wykonywanych za wyraźną zgodą właściciela danych.

❌ Nie używaj tego projektu do prób uzyskania nieautoryzowanego dostępu do cudzych baz danych.

Użytkownik ponosi pełną odpowiedzialność za sposób użycia. Działania niezgodne z prawem lub bez zgody właściciela danych są zabronione.

## Jak to działa

Skrypt:
1. Otwiera plik `passwords.txt` z listą haseł.
2. Testuje kolejne hasła na bazie KeePass (`.kdbx`).
3. Zatrzymuje się po znalezieniu poprawnego hasła.

## Wymagania

- Python 3.x
- zależności z `requirements.txt`

Instalacja:

```bash
pip install -r requirements.txt
```

## Użycie

1. Upewnij się, że plik bazy (domyślnie `DATABASE.kdbx`) jest dostępny w katalogu projektu.
2. Przygotuj `passwords.txt` (jedno hasło w linii).
3. Uruchom:

```bash
python script.py
```

## Uwagi

- Projekt ma charakter edukacyjny i recovery/security-testing dla legalnych scenariuszy.
- Jeśli chcesz, możesz dostosować nazwę bazy i ścieżki plików bezpośrednio w `script.py`.
