"""
=================================================================================================
Zadanie 1: Odczyt i zapis do pliku tekstowego

Stwórz plik tekstowy dane.txt zawierający kilka linijek tekstu (np. imiona).
Napisz program, który:
Odczyta zawartość pliku i wyświetli ją w konsoli.
Dopisze na końcu pliku tekst: "Dodano nową linię!".
Ponownie wyświetli całą zawartość pliku po aktualizacji. 
"""

with open("dane.txt", "r") as file:
    content = file.read()
    print("Zawartość pliku przed dopisaniem:")
    print(content)

with open("dane.txt", "a") as file:
    file.write("\nDodano nową linię!")

with open("dane.txt", "r") as file:
    updated_content = file.read()
    print("\nZawartość pliku po dopisaniu:")
    print(updated_content)


""" 
=================================================================================================
Zadanie 2: Licznik słów w pliku

Stwórz plik tekst.txt z dowolnym tekstem (np. artykułem).
Napisz program, który:
Odczyta plik.
Policzy, ile słów znajduje się w pliku.
Wyświetli wyniki w formacie: "Liczba słów w pliku: X".
Hint: wykorzystaj funkcje .split()
"""

with open("tekst.txt", "r") as file:
    content = file.read()
    word_count = len(content.split())
    print(f"Liczba słów w pliku: {word_count}")

""" 
=================================================================================================
Zadanie 3: Kopiowanie zawartości pliku

Stwórz plik oryginal.txt z dowolnym tekstem.
Napisz program, który:
Odczyta zawartość oryginal.txt.
Utworzy nowy plik kopia.txt i zapisze w nim zawartość pliku oryginal.txt.
"""

with open("oryginal.txt", "r") as original_file:
    content = original_file.read()

with open("kopia.txt", "w") as copy_file:
    copy_file.write(content)

print("Plik został skopiowany do 'kopia.txt'.")


""" 
=================================================================================================
Zadanie 4: Filtracja danych w pliku

Stwórz plik liczby.txt, który zawiera liczby (każda liczba w osobnej linii).
Napisz program, który:
Odczyta plik.
Wyfiltruje tylko liczby parzyste i zapisze je do nowego pliku parzyste.txt.
Hint: wykorzystaj funkcje .strip()
"""

with open("liczby.txt", "r") as file:
    numbers = file.readlines()

even_numbers = [num.strip() for num in numbers if int(num.strip()) % 2 == 0]

with open("parzyste.txt", "w") as even_file:
    even_file.write("\n".join(even_numbers))

print("Liczby parzyste zostały zapisane do 'parzyste.txt'.")

"""
=================================================================================================
Zadanie 5: Połączenie kilku plików w jeden

Stwórz trzy pliki tekstowe (plik1.txt, plik2.txt, plik3.txt), każdy zawierający kilka linijek tekstu.
Napisz program, który:
Odczyta zawartość wszystkich trzech plików.
Połączy ich zawartość w jeden plik polaczony.txt, dodając między nimi separator, np. "=====". 
"""
files_to_merge = ["plik1.txt", "plik2.txt", "plik3.txt"]

with open("polaczony.txt", "w") as merged_file:
    for file_name in files_to_merge:
        with open(file_name, "r") as file:
            content = file.read()
            merged_file.write(content)
            merged_file.write("\n=====\n")

print("Pliki zostały połączone w 'polaczony.txt'.")
