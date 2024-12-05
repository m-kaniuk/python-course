import requests

BASE_URL = "https://reqres.in/api/users"

new_user = {
    "name": "Jan Kowalski",
    "job": "developer"
}

response = requests.post(BASE_URL, json=new_user)

if response.status_code == 201:
    data = response.json()
    print("Użytkownik został utworzony:")
    print(f"ID: {data['id']}")
    print(f"Utworzony o: {data['createdAt']}")
else:
    print("Nie udało się utworzyć użytkownika.")
