# action-analyser

## Wymagania:
1. Python 3.9
2. `pip` - domyślny menadżer pakietów Python.

*Sugerowana instalacja w środowisku wirtualnym (virtualenv)*

## Instalacja

Aby zainstalować zależności projektu, należy:
1. Zainstalować *wheel* do biblioteki `TA-Lib`. Aby to zrobić, należy wykonać
(z poziomu folderu projektu):
```shell
pip install ./lib/TA-Lib.whl
```

2. Zainstalować wymagania z pliku `requirements.txt`
```shell
pip install -r ./requirements.txt
```

Aby uruchomić program, należy wykonać plik `app.py`.

## Dodatkowe informacje
* Do poprawnego działania aplikacji konieczne jest podanie pliku, zawierającego kolumny:
  * `Date`
  * `Open`
  * `High`
  * `Low`
  * `Close`
  * `Volume`
* Program nie sprawdza poprawności wgranego pliku.
* Prostą metodą generowania takich plików jest skorzystanie z biblioteki `yfinance`.
Przykładowy sposób tworzenia pliku i generowania wykresu na jego podstawie znajduje 
się w pliku `generate_data.py`, natomiast przykładowe wygenerowane pliki — w folderze `samples`.