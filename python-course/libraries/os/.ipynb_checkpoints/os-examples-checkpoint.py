import os
import time

# 1. Utworzenie nowego katalogu
new_directory = "example_directory"
if not os.path.exists(new_directory):
    os.mkdir(new_directory)
    print(f"Katalog '{new_directory}' został utworzony.")
else:
    print(f"Katalog '{new_directory}' już istnieje.")

# 2. Wyświetlenie plików i katalogów w bieżącym katalogu
print("\nPliki i katalogi w bieżącym katalogu:")
for item in os.listdir("."):
    print(item)

# 3. Utworzenie nowego pliku w nowym katalogu
file_path = os.path.join(new_directory, "example_file.txt")
with open(file_path, "w") as file:
    file.write("To jest przykładowy plik.")
print(f"\nPlik '{file_path}' został utworzony.")

time.sleep(5)

# 4. Usunięcie pliku i katalogu
os.remove(file_path)
print(f"\nPlik '{file_path}' został usunięty.")
os.rmdir(new_directory)
print(f"Katalog '{new_directory}' został usunięty.")
