""" 
=================================================================================================
Zadanie 1: Uzupełnij funkcję divide_numbers blokiem try-except-else-finally
"""


def divide_numbers(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Błąd: Dzielenie przez zero!")
    else:
        print(f"Wynik: {result}")
    finally:
        print("Operacja zakończona.")


divide_numbers(10, 2)
divide_numbers(10, 0)


""" 
=================================================================================================
Zadanie 2: Uzupełnij funkcję get_list_element blokiem try-except-else-finally
"""


def get_list_element(my_list, index):
    try:
        element = my_list[index]
    except IndexError:
        print(f"Błąd: Indeks {index} jest poza zakresem listy.")
    else:
        print(f"Element at index {index}: {element}")
    finally:
        print("Operacja zakończona.")


my_list = [1, 2, 3, 4, 5]
get_list_element(my_list, 3)
get_list_element(my_list, 10)


""" 
=================================================================================================
Zadanie 3: Uzupełnij funkcję get_dict_value blokiem try-except-else-finally
"""


def get_dict_value(my_dict, key):
    try:
        value = my_dict[key]
    except KeyError:
        print(f"Błąd: Klucz '{key}' nie istnieje w słowniku.")
    else:
        print(f"Wartość dla klucza {key}: {value}")
    finally:
        print("Operacja zakończona.")


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
    try:
        num1 = float(input("Podaj pierwszą liczbę: "))
        num2 = float(input("Podaj drugą liczbę: "))
        operation = input("Podaj operację (+, -, *, /): ")

        if operation == "+":
            result = num1 + num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "*":
            result = num1 * num2
        elif operation == "/":
            result = num1 / num2
        else:
            raise ValueError("Nieznana operacja")
    except ZeroDivisionError:
        print("Błąd: Dzielenie przez zero!")
    except ValueError as e:
        print(f"Błąd: {e}")
    else:
        print(f"Wynik: {result}")
    finally:
        print("Koniec obliczeń")


calculator()
