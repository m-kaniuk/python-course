"""
=================================================================================================
Otwieranie pliku w trybie zapisu
"""

with open("example.txt", "w") as file:
    file.write("To jest zapisany tekst.\nKolejna linia tekstu.")

"""
=================================================================================================
Otwieranie pliku w trybie odczytu
"""

with open("example.txt", "r") as file:
    content = file.read()
    print(content)


"""
=================================================================================================
Otwieranie pliku w trybie dopisywania
"""

with open("example.txt", "a") as file:
    file.write("\nDodano tę linię.")


"""
=================================================================================================
Otwieranie pliku w trybie odczytu
"""

with open("example.txt", "r") as file:
    for line in file:
        print(line.strip())  # Wyświetlenie linii bez końcowego znaku nowej linii


"""
=================================================================================================
Zapis w trybie binarnym
"""

with open("python.png", "rb") as src_file:
    data = src_file.read()

"""
=================================================================================================
Zapisanie danych binarnych do nowego pliku.

"""

with open("copy.png", "wb") as dest_file:
    dest_file.write(data)
