import requests

# URL API, do którego wykonujemy żądanie GET
url = "https://jsonplaceholder.typicode.com/posts"

# Wykonanie żądania GET do API
response = requests.get(url)

# Sprawdzenie, czy żądanie zakończyło się sukcesem (kod statusu 200)
if response.status_code == 200:
    # Przetworzenie odpowiedzi JSON
    data = response.json()

    # Wyświetlenie pierwszych 5 wpisów
    print("Pierwsze 5 wpisów z API:")
    for post in data[:5]:
        print(f"ID: {post['id']}, Tytuł: {post['title']}")
else:
    print(f"Żądanie nie powiodło się z kodem statusu: {response.status_code}")
