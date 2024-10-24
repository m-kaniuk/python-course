# Ćwiczenie 1: Instrukcje warunkowe
# Napisz program, który sprawdza, czy liczba a jest dodatnia, ujemna, czy równa zero i wyświetla odpowiedni komunikat.

a = 10

if a > 0:
    print("The number is positive")
elif a < 0:
    print("The number is negative")
else:
    print("The number is zero")

# Ćwiczenie 2: Pętla `while`
# Napisz program, który wypisuje liczby od 1 do 5 używając pętli `while`.

i = 1

while i <= 5:
    print(i)
    i += 1

# Ćwiczenie 3: Pętla `for`
# Napisz program, który wypisuje wszystkie elementy z listy `numbers`.

numbers = [1, 2, 3, 4, 5]

for number in numbers:
    print(number)

# Ćwiczenie 4: Pętla `for` z funkcją `range`
# Napisz program, który wypisuje liczby od 0 do 9 używając funkcji `range`.

for i in range(10):
    print(i)

# Ćwiczenie 5: Instrukcja `break`
# Napisz program, który przerywa pętlę, gdy znajdzie liczbę 3 na liście `numbers`.

numbers = [1, 2, 3, 4, 5]

for number in numbers:
    if number == 3:
        break
    print(number)

# Ćwiczenie 6: Instrukcja `continue`
# Napisz program, który pomija liczbę 3 na liście `numbers` i wypisuje pozostałe liczby.

numbers = [1, 2, 3, 4, 5]

for number in numbers:
    if number == 3:
        continue
    print(number)

# Ćwiczenie 7: Pętla `for` z instrukcją `else`
# Napisz program, który sprawdza, czy liczba 6 znajduje się na liście `numbers`. Jeśli nie, wypisuje komunikat "Liczba 6 nie została znaleziona".

numbers = [1, 2, 3, 4, 5]

for number in numbers:
    if number == 6:
        print("Number 6 found")
        break
else:
    print("Number 6 not found")

# Ćwiczenie 8: Zagnieżdżone pętle
# Napisz program, który wypisuje tabliczkę mnożenia od 1 do 3.

for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i} * {j} = {i * j}")

# Ćwiczenie 9: Instrukcja `pass`
# Napisz program, który zawiera pustą funkcję `my_function` z użyciem instrukcji `pass`.

def my_function():
    pass

my_function()

# Ćwiczenie 10: Obsługa wyjątków
# Napisz program, który próbuje podzielić liczby a przez b i obsługuje przypadek dzielenia przez zero.

a = 10
b = 0

try:
    result = a / b
except ZeroDivisionError:
    print("Error: Division by zero")
else:
    print("Result:", result)
finally:
    print("End of program")
