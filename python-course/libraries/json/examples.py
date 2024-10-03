import json

# 1. Zakodowanie danych do formatu JSON
data = {
    "imie": "Jan",
    "wiek": 30,
    "miasto": "Warszawa",
    "umiejętności": ["Python", "Java", "C++"],
}

json_data = json.dumps(data)
print("Zakodowane dane w formacie JSON:")
print(json_data)

# Zapisanie danych JSON do pliku
with open("dane.json", "w") as file:
    json.dump(data, file)
    print("\nDane zostały zapisane do pliku 'dane.json'.")

# 2. Zdekodowanie danych z formatu JSON
decoded_data = json.loads(json_data)
print("\nZdekodowane dane z formatu JSON:")
print(decoded_data)

# Odczytanie danych JSON z pliku
with open("dane.json", "r") as file:
    file_data = json.load(file)
    print("\nDane odczytane z pliku 'dane.json':")
    print(file_data)
