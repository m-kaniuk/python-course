"""
Zadanie 1: Parsowanie złożonych struktur JSON

Napisz funkcję parse_json, która przyjmuje ciąg znaków w formacie JSON zawierający słownik i zwraca wartość dla podanego klucza. Do testowania użyj podanego json_str.
"""

json_str = """
{
    "id": 123,
    "name": "Alice",
    "age": 30,
    "email": "alice@example.com",
    "address": {
        "street": "123 Main St",
        "city": "Wonderland",
        "postal_code": "12345"
    },
    "preferences": {
        "notifications": true,
        "newsletter": false
    },
    "friends": [
        {
            "id": 456,
            "name": "Bob",
            "age": 25
        },
        {
            "id": 789,
            "name": "Charlie",
            "age": 35
        }
    ]
}

"""
