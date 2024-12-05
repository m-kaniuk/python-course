import requests

BASE_URL = "https://reqres.in/api/users/2"

updated_user = {
    "name": "Jan Kowalski",
    "job": "senior developer"
}

response = requests.put(BASE_URL, json=updated_user)

if response.status_code == 200:
    data = response.json()
    print("Dane użytkownika zostały zaktualizowane:")
    print(f"Nazwa: {data['name']}")
    print(f"Praca: {data['job']}")
    print(f"Ostatnia aktualizacja: {data['updatedAt']}")
else:
    print("Nie udało się zaktualizować danych użytkownika.")
