import json
from urllib.parse import urlparse

import requests

API_TOKEN = "<token>"

headers = {
    "Authorization": f"Bearer {API_TOKEN}",
    "Content-Type": "application/json",
}

# Ustawienia
url = f"https://app.eu0.signalfx.com/v2"

# Funkcja pomocnicza do wysyłania żądań HTTP i drukowania wyników
def send_request(response):
    print(f"Status Code: {response.status_code}")
    print(f"Headers: {response.headers}")
    try:
        data = response.json()
        print(f"Body (JSON): {json.dumps(data, indent=2)}")
    except ValueError:
        print(f"Body (Text): {response.text}")


# GET Request with Headers
print("--- Request with Headers ---")
response = requests.get(f"{url}/chart", headers=headers)
send_request(response)

# Request with Query Parameters
print("--- Request with Query Parameters ---")
params = {"name": "AWS CloudWatch metric API calls (rate/min)"}
response = requests.get(f"{url}/chart", headers=headers, params=params)
send_request(response)

# Handling Cookies and Sessions
print("--- Handling Cookies and Sessions ---")
session = requests.Session()
response = session.get(f"{url}/chart", headers=headers)
send_request(response)
print("Cookies:", session.cookies.get_dict())

# Bearer Token Authentication
print("--- Bearer Token Authentication ---")
token = API_TOKEN
headers = {"Authorization": f"Bearer {token}"}
response = requests.get(f"{url}/chart", headers=headers)
send_request(response)

# Setting Timeout
print("--- Setting Timeout ---")
timeout_url = "http://192.0.2.123"
try:
    response = requests.get(f"{timeout_url}", timeout=10)
    send_request(response)
except requests.Timeout:
    print("Request timed out")

# Handling Redirects
print("--- Handling Redirects ---")
redirect_url = "http://httpbin.org/redirect/1"
response = requests.get(redirect_url)
send_request(response)

# urllib.parse - Parsowanie URL-a
parsed_url = urlparse(url)
print("urllib.parse - Full URL:", url)
print("urllib.parse - Scheme:", parsed_url.scheme)
print("urllib.parse - Netloc:", parsed_url.netloc)
print("urllib.parse - Path:", parsed_url.path)