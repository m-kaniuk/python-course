"""
=================================================================================================
Podstawowy przykład użycia try-except:
"""

try:
    # Próba wykonania kodu, który może zgłosić wyjątek
    result = 10 / 0
except ZeroDivisionError as e:
    # Obsługa wyjątku
    print(f"Error: {e}")

""" 
=================================================================================================
Przykład z try-except-else-finally:
"""

try:
    # Próba wykonania kodu, który może zgłosić wyjątek
    result = 10 / 2
except ZeroDivisionError as e:
    # Obsługa wyjątku
    print(f"Error: {e}")
else:
    # Kod, który wykona się, jeśli nie wystąpił wyjątek
    print(f"Result: {result}")
finally:
    # Kod, który wykona się niezależnie od tego, czy wystąpił wyjątek, czy nie
    print("Execution completed")

""" 
=================================================================================================
Przykład z różnymi typami wyjątków:
"""
try:
    # Próba wykonania kodu, który może zgłosić wyjątek
    value = int(input("Podaj liczbę: "))
    result = 10 / value
except ZeroDivisionError as e:
    # Obsługa wyjątku dzielenia przez zero
    print(f"Error: Dzielenie przez zero - {e}")
except ValueError as e:
    # Obsługa wyjątku nieprawidłowej wartości
    print(f"Error: Nieprawidłowa wartość - {e}")
else:
    # Kod, który wykona się, jeśli nie wystąpił wyjątek
    print(f"Result: {result}")
finally:
    # Kod, który wykona się niezależnie od tego, czy wystąpił wyjątek, czy nie
    print("Execution completed")

"""
=================================================================================================
Podnoszenie wyjątków
"""


def check_age(age):
    if age < 18:
        raise ValueError("Wiek musi być większy lub równy 18.")
    else:
        print("Wiek jest odpowiedni.")


try:
    check_age(15)
except ValueError as e:
    print(f"Wystąpił błąd: {e}")

"""
=================================================================================================
Ponownie podniesienie wyjątku
"""


def divide(a, b):
    try:
        if b == 0:
            raise ZeroDivisionError("Dzielenie przez zero!")
        return a / b
    except ZeroDivisionError as e:
        print(f"Obsługa błędu wewnątrz funkcji: {e}.")
        raise  # Ponowne podniesienie wyjątku


try:
    result = divide(10, 0)
except ZeroDivisionError as e:
    print(f"Wystąpił błąd: {e}")
