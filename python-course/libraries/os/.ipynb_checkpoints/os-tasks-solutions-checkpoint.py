"""
Zadanie 1: Sprawdzanie obecności pliku

Opis zadania:
Napisz funkcję check_file_exists, która przyjmuje ścieżkę do pliku jako argument i zwraca True, jeśli plik istnieje, w przeciwnym razie zwraca False.
"""

import os

def check_file_exists(file_path):
    return os.path.isfile(file_path)

# Przykład użycia
file_path = "os-examples.py"
exists = check_file_exists(file_path)
print(exists)  # Powinno zwrócić True lub False w zależności od obecności pliku

"""
Zadanie 2: Tworzenie katalogu

Opis zadania:
Napisz funkcję create_directory, która przyjmuje ścieżkę do katalogu jako argument i tworzy ten katalog, jeśli nie istnieje.
"""

import os

def create_directory(dir_path):
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
        return True
    return False

# Przykład użycia
dir_path = "new_folder"
created = create_directory(dir_path)
print(created)  # Powinno zwrócić True jeśli katalog został utworzony, False jeśli już istnieje

