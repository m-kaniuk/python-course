"""
=================================================================================================
Zadanie 1: Wartości domyślne w funkcji
Napisz funkcję, która oblicza cenę po rabacie. Funkcja powinna przyjmować cenę oryginalną
oraz opcjonalny procent rabatu (domyślnie 10%).
"""


def oblicz_cene_po_rabacie(cena, procent_rabatu=10):
    rabat = cena * (procent_rabatu / 100)
    cena_po_rabacie = cena - rabat
    return cena_po_rabacie


# Przykładowe użycie funkcji
oryginalna_cena = 100
procent_rabatu = 15

cena_po_rabacie = oblicz_cene_po_rabacie(oryginalna_cena, procent_rabatu)
print(f"Oryginalna cena: {oryginalna_cena} zł")
print(f"Procent rabatu: {procent_rabatu}%")
print(f"Cena po rabacie: {cena_po_rabacie} zł")

# Użycie funkcji z domyślnym rabatem
cena_po_rabacie_domyslna = oblicz_cene_po_rabacie(oryginalna_cena)
print(f"Oryginalna cena: {oryginalna_cena} zł")
print("Procent rabatu: 10% (domyślny)")
print(f"Cena po rabacie: {cena_po_rabacie_domyslna} zł")

"""
=================================================================================================
Zadanie 2: Wartość domyślna
Napisz funkcję, która przyjmuje liczbę i podnosi ją do kwadratu,
chyba że podany jest drugi parametr określający inną potęgę.
"""


def podnies_do_potegi(liczba, potega=2):
    return liczba**potega


# Przykładowe użycie funkcji
liczba = 5

# Podniesienie do kwadratu (domyślna potęga)
wynik_kwadrat = podnies_do_potegi(liczba)
print(f"Liczba {liczba} podniesiona do kwadratu to: {wynik_kwadrat}")

# Podniesienie do trzeciej potęgi
potega = 3
wynik_potega = podnies_do_potegi(liczba, potega)
print(f"Liczba {liczba} podniesiona do potęgi {potega} to: {wynik_potega}")


"""
=================================================================================================
Zadanie 3: Zwracanie wielu wartości
Napisz funkcję, która przyjmuje listę liczb i zwraca zarówno ich sumę, jak i średnią arytmetyczną.
"""


def suma_i_srednia(*args):
    suma = sum(args)
    srednia = suma / len(args) if args else 0
    return suma, srednia


suma, średnia = suma_i_srednia(22, 55, 342, 634, 1, 123, 62, 1)
print(f"{suma=} {średnia=}")

"""
=================================================================================================
## Zadanie 4: Liczenie Wystąpień Litery
Napisz funkcję, która przyjmuje ciąg znaków (tekst) oraz literę i zwraca liczbę wystąpień podanej litery.

1. Utwórz funkcję licz_wystapienia_litery(tekst, litera), która przyjmuje jeden ciąg znaków i szukaną literę.
2. Policz wystąpienia każdej litery.
3. Przetestuj funkcję na kilku przykładach.
"""


def licz_wystapienia_litery(tekst, szukana_litera):
    wystapienia = 0
    for litera_w_tekscie in tekst:
        if litera_w_tekscie == szukana_litera:
            wystapienia += 1
    return wystapienia


# Przykładowe użycie
tekst = "to jest test to jest tylko test"
print(licz_wystapienia_litery(tekst, "t"))
# Output: 9


"""
=================================================================================================
Zadanie 5: Suma Kwadratów Liczb
Napisz funkcję, która przyjmuje listę liczb i zwraca sumę ich kwadratów.

1. Utwórz funkcję suma_kwadratow(lista_liczb), która przyjmuje listę liczb lista_liczb.
2. Oblicz sumę kwadratów liczb z listy.
3. Przetestuj funkcję dla kilku list liczb.
"""


def suma_kwadratow(lista_liczb):
    return sum(x**2 for x in lista_liczb)


# Przykładowe użycie
print(suma_kwadratow([1, 2, 3, 4, 5]))  # Output: 55
print(suma_kwadratow([0, -1, -2]))  # Output: 5


"""
=================================================================================================
Zadanie 6: Obliczanie Silni Rekurencją
Napisz funkcję, która oblicza silnię (factorial) liczby całkowitej za pomocą rekurencji.

1. Utwórz funkcję silnia(n), która przyjmuje jedną liczbę całkowitą n.
2. Zaimplementuj rekurencyjny algorytm obliczania silni:
3. Jeśli n jest równe 0 lub 1, zwróć 1 (silnia 0 i 1 to 1).
4. W przeciwnym razie, zwróć n pomnożone przez wynik wywołania silnia(n-1).
5. Przetestuj funkcję dla kilku wartości n.
"""


def silnia(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * silnia(n - 1)


# Przykładowe użycie
print(silnia(5))  # Output: 120
print(silnia(0))  # Output: 1
print(silnia(1))  # Output: 1
print(silnia(6))  # Output: 720
print(silnia(3))  # Output: 6


"""
=================================================================================================
Zadanie z Lambdą: Obliczenie Funkcji x^3 + 8y^2 + 2z + 6
Napisz funkcję, która przyjmuje trzy argumenty: x, y i z, 
a następnie zwraca wynik wyrażenia x^3 + 8y^2 + 2z + 6, używając funkcji lambda.

1. Zdefiniuj funkcję lambda, która oblicza wartość wyrażenia x^3 + 8y^2 + 2z + 6.
2. Zwróć wynik obliczenia.
3. Przetestuj funkcję na kilku przykładach.
"""

funkcja = lambda x, y, z: x**3 + 8 * y**2 + 2 * z + 6

# Przykładowe użycie
print(funkcja(1, 2, 3))  # Output: 41
print(funkcja(0, 0, 0))  # Output: 6
print(funkcja(2, 1, 4))  # Output: 30
print(funkcja(-1, 2, -3))  # Output: 43
print(funkcja(3, 2, 1))  # Output: 117
