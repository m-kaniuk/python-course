"""
Funkcje w Pythonie: Przykłady i Wyjaśnienia
Funkcje w Pythonie są definiowane za pomocą słowa kluczowego `def`.
Mogą przyjmować parametry, wykonywać operacje i zwracać wartości.
Poniżej znajdują się przykłady różnych typów funkcji w Pythonie.
"""

"""
=================================================================================================
PRZYKŁAD 1: Podstawowa Funkcja
To jest podstawowa funkcja, która nie przyjmuje żadnych parametrów i zwraca string.
"""


def greet():
    return "Hello, World!!!"


print(greet())  # Output: Hello, World!


def greet_person(name, city):
    return f"Hello, {name} from {city}!!!"


print(greet_person("Jan", "Kraków"))  # Output: Hello, Jan from Kraków!!!


"""
=================================================================================================
PRZYKŁAD 2: Funkcja z Parametrami
Funkcje mogą przyjmować parametry, aby były bardziej elastyczne.
"""


def add(a, b):
    return a + b


print(add(a=1, b=2))
print(add(4, 2))

# Wywołanie funkcji
print(add(3, 5))  # Output: 8
print(add(-1, 7))  # Output: 6


def divide(numerator, denominator):
    return numerator / denominator


print(divide(denominator=2, numerator=6))  # Output: 3.0


"""
=================================================================================================
PRZYKŁAD 3: Funkcja z Parametrami Domyślnymi
Możesz zdefiniować domyślne wartości dla parametrów.
"""


def greet(name="World"):
    return f"Hello, {name}!"


# Wywołanie funkcji
print(greet())  # Output: Hello, World!
print(greet("Alice"))  # Output: Hello, Alice!


"""
=================================================================================================
PRZYKŁAD 4: Funkcje Lambda
Funkcje Lambda to małe anonimowe funkcje definiowane za pomocą słowa kluczowego `lambda`.
Mogą mieć dowolną liczbę argumentów, ale tylko jedno wyrażenie.
"""

add = lambda x, y: x + y

# Wywołanie funkcji lambda
print(add(3, 5))  # Output: 8


"""
=================================================================================================
PRZYKŁAD 5: Funkcje Wyższego Rzędu
Funkcje, które przyjmują inne funkcje jako argumenty lub je zwracają, są znane jako funkcje wyższego rzędu.
"""


def apply_func(func, value):
    return func(value)


def square(x):
    return x**2


# Wywołanie funkcji wyższego rzędu
print(apply_func(square, 4))  # Output: 16


"""
=================================================================================================
PRZYKŁAD 6: Rekurencja
Funkcja może wywoływać samą siebie. Jest to znane jako rekurencja. Poniższy przykład oblicza silnię liczby.
"""


def factorial(n):
    if n < 2:
        return 1
    else:
        return n * factorial(n - 1)


# Wywołanie funkcji rekurencyjnej
print(factorial(0))  # Output: 120


"""
=================================================================================================
PRZYKŁAD 7: Pass by value
"""


def modify_immutable(x):
    x += 10  # Tworzenie nowej lokalnej zmiennej
    print(f"Inside function: {x}")  # Output: Inside function: 10


a = 5
print(f"Before: {a}")  # Output: Before: 5
modify_immutable(a)
print(f"After: {a}")  # Output: After: 5


"""
=================================================================================================
PRZYKŁAD 8: Pass by reference
"""


def modify_mutable(lst):
    lst.append(4)  # Modyfikacja oryginalnej listy
    print(f"Inside function: {lst}")  # Output: Inside function: [1, 2, 3, 4]


my_list = [1, 2, 3]
print(f"Before: {my_list}")  # Output: Before: [1, 2, 3]
modify_mutable(my_list)
print(f"After: {my_list}")  # Output: After: [1, 2, 3, 4]
