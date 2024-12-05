import requests

BASE_URL = "https://reqres.in/api/users"

response = requests.get(BASE_URL, params={"page": 1})

if response.status_code == 200:
    data = response.json()
    print("Lista użytkowników:")
    for user in data["data"]:
        print(f"{user['first_name']} {user['last_name']} - {user['email']}")
else:
    print("Nie udało się pobrać listy użytkowników.")
