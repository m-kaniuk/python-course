import argparse

# Tworzenie parsera
parser = argparse.ArgumentParser(description="Przykładowy program z argparse")

# Dodanie argumentów
parser.add_argument("liczba", type=int, help="Podaj liczbę całkowitą")  # Argument pozycyjny
parser.add_argument("--verbose", action="store_true", help="Włącz tryb szczegółowy")  # Opcjonalny

# Parsowanie argumentów
args = parser.parse_args()

# Dostęp do przekazanych wartości
print(f"Podana liczba: {args.liczba}")
if args.verbose:
    print("Tryb szczegółowy włączony!")

