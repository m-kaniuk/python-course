'''
# Zadanie 1: Liczenie do podanej liczby

Opis: Program wypisuje wszystkie liczby od 1 do podanej liczby.
'''

import argparse

# Tworzenie parsera
parser = argparse.ArgumentParser(description="Program liczący do podanej liczby")

# Dodanie argumentu
parser.add_argument("number", type=int, help="Podaj liczbę całkowitą, do której mam liczyć")

# Parsowanie argumentów
args = parser.parse_args()

# Liczenie do podanej liczby
for i in range(1, args.number + 1):
    print(i)


'''
Zadanie 2: Konwersja temperatury

Opis: Program konwertuje temperaturę z Celsjusza na Fahrenheita lub odwrotnie.

Hint: °F = °C × (9/5) + 32
'''

# Tworzenie parsera
parser = argparse.ArgumentParser(description="Program do konwersji temperatur")

# Dodanie argumentów
parser.add_argument("temperature", type=float, help="Podaj temperaturę do konwersji")
parser.add_argument("--to-fahrenheit", action="store_true", help="Konwertuj z Celsjusza na Fahrenheita")

# Parsowanie argumentów
args = parser.parse_args()

# Konwersja temperatury
if args.to_fahrenheit:
    converted = (args.temperature * 9/5) + 32
    print(f"{args.temperature}°C to {converted:.2f}°F")
else:
    converted = (args.temperature - 32) * 5/9
    print(f"{args.temperature}°F to {converted:.2f}°C")
