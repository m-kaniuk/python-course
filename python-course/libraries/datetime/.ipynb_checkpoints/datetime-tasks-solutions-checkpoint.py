"""
Zadanie 1: Zmiana formatowania daty
Opis zadania:
Napisz funkcję reformat_date, która przyjmuje datę w formacie MM/DD/YYYY i zwraca ją w formacie YYYY-MM-DD.
"""

from datetime import datetime

def reformat_date(date_str):
    # Definiowanie oryginalnego formatu daty
    original_format = "%m/%d/%Y"
    # Konwersja daty z oryginalnego formatu do obiektu datetime
    date_obj = datetime.strptime(date_str, original_format)
    # Definiowanie nowego formatu daty
    new_format = "%Y-%m-%d"
    # Formatowanie daty do nowego formatu
    formatted_date = date_obj.strftime(new_format)
    return formatted_date

# Przykład użycia
original_date = "08/07/2023"
formatted_date = reformat_date(original_date)
print(formatted_date)  # Powinno zwrócić "2023-08-07"


"""
Zadanie 2: Obliczanie wieku w dniach
Opis zadania:
Uzupełnij funkcję calculate_age, która przyjmuje datę urodzenia w formacie YYYY-MM-DD i zwraca wiek w dniach.
"""

from datetime import datetime

def calculate_age(birthdate_str):
    birthdate_format = "%Y-%m-%d"
    birthdate = datetime.strptime(birthdate_str, birthdate_format)
    today = datetime.today()
    age_in_days = (today - birthdate).days
    return age_in_days

# Przykład użycia
birthdate = "1990-08-07"
age_in_days = calculate_age(birthdate)
print(age_in_days)  # Zwraca wiek w dniach na podstawie dzisiejszej daty
