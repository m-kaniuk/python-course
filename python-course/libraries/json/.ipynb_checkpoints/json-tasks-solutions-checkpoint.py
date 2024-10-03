"""
Zadanie 1: Parsowanie złożonych struktur JSON

Opis zadania:
Napisz funkcję parse_json, która przyjmuje ciąg znaków w formacie JSON zawierający słownik i zwraca wartość dla podanego klucza.
"""

import json

def parse_json(json_str, key):
    data = json.loads(json_str)
    return data[key]

json_str = '''
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

'''

print(parse_json(json_str, "preferences")["newsletter"])