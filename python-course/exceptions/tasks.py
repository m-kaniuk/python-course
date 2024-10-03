""" 
=================================================================================================
Zadanie 1: Uzupełnij funkcję divide_numbers blokiem try-except-else-finally
"""


def divide_numbers(a, b):
    result = a / b
    print(f"Wynik: {result}")


divide_numbers(10, 2)
divide_numbers(10, 0)


""" 
=================================================================================================
Zadanie 2: Uzupełnij funkcję get_list_element blokiem try-except-else-finally
"""


def get_list_element(my_list, index):
    element = my_list[index]
    print(f"Element at index {index}: {element}")


my_list = [1, 2, 3, 4, 5]
get_list_element(my_list, 3)
get_list_element(my_list, 10)


""" 
=================================================================================================
Zadanie 3: Uzupełnij funkcję get_dict_value blokiem try-except-else-finally
"""


def get_dict_value(my_dict, key):
    value = my_dict[key]
    print(f"Wartość dla klucza {key}: {value}")


my_dict = {"name": "Jan", "age": 30}
get_dict_value(my_dict, "name")
get_dict_value(my_dict, "address")


""" 
=================================================================================================
Zadanie 4: Kalkulator z obsługą błędów
Napisz program kalkulatora, który wykonuje podstawowe operacje matematyczne:
(dodawanie, odejmowanie, mnożenie, dzielenie). Obsłuż błędy takie jak: dzielenie przez zero, 
nieprawidłowe wejście użytkownika (np. litery zamiast liczb).

Wskazówki:

Użyj try-except do obsługi wyjątków.

Użyj else, aby wykonać kod tylko wtedy, gdy nie wystąpił wyjątek.

Użyj finally do wyświetlenia komunikatu końcowego.
"""


def calculator():
    num1 = float(input("Podaj pierwszą liczbę: "))
    num2 = float(input("Podaj drugą liczbę: "))
    operation = input("Podaj operację (+, -, *, /): ")


calculator()
