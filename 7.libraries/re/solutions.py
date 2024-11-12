"""
Zadanie 1: Walidacja adresu e-mail

Napisz funkcję is_valid_email, która przyjmuje adres e-mail jako argument i zwraca True, jeśli adres jest poprawny, w przeciwnym razie zwraca False. Użyj wyrażenia regularnego do walidacji adresu e-mail.
"""

import re


def is_valid_email(email):
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return re.match(pattern, email) is not None


# Przykład użycia
email = "test@example.com"
print(is_valid_email(email))  # Powinno zwrócić True

email = "invalid-email"
print(is_valid_email(email))  # Powinno zwrócić False


"""
Zadanie 2: Wyszukiwanie numerów telefonów

Napisz funkcję find_phone_numbers, która przyjmuje tekst jako argument i zwraca listę wszystkich numerów telefonów w formacie XXX-XXX-XXX znalezionych w tym tekście.
"""

import re


def find_phone_numbers(text):
    pattern = r"\b\d{3}-\d{3}-\d{3}\b"
    return re.findall(pattern, text)


# Przykład użycia
text = "Contact us at 123-456-790 or 987-654-310."
print(find_phone_numbers(text))  # Powinno zwrócić ['123-456-790', '987-654-310']
