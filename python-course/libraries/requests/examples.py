import json
from urllib.parse import urlparse

import requests
from requests.auth import HTTPBasicAuth
from requests.exceptions import HTTPError, RequestException

# Ustawienia
url = "http://api.open-notify.org/astros.json"
post_url = "https://httpbin.org/post"  # Używane do przykładu POST
file_url = "https://httpbin.org/post"  # Używane do przykładu wysyłania plików
auth_url = "https://httpbin.org/basic-auth/user/passwd"


# Funkcja pomocnicza do wysyłania żądań HTTP i drukowania wyników
def send_request(response):
    print(f"Status Code: {response.status_code}")
    print(f"Headers: {response.headers}")
    try:
        data = response.json()
        print(f"Body (JSON): {json.dumps(data, indent=2)}")
    except ValueError:
        print(f"Body (Text): {response.text}")


# GET Request
print("--- GET Request ---")
response = requests.get(url)
send_request(response)

# Request with Headers
print("--- Request with Headers ---")
headers = {"User-Agent": "Mozilla/5.0"}
response = requests.get(url, headers=headers)
send_request(response)

# Request with Query Parameters
print("--- Request with Query Parameters ---")
params = {"param1": "value1", "param2": "value2"}
response = requests.get(url, params=params)
send_request(response)

# Handling Cookies and Sessions
print("--- Handling Cookies and Sessions ---")
session = requests.Session()
response = session.get(url)
send_request(response)
print("Cookies:", session.cookies.get_dict())

# Basic Authentication
print("--- Basic Authentication ---")
response = requests.get(auth_url, auth=HTTPBasicAuth("user", "passwd"))
send_request(response)

# Bearer Token Authentication
print("--- Bearer Token Authentication ---")
token = "YOUR_BEARER_TOKEN"
headers = {"Authorization": f"Bearer {token}"}
response = requests.get(url, headers=headers)
send_request(response)

# Handling JSON Data
print("--- Handling JSON Data ---")
response = requests.get(url)
send_request(response)

# Setting Timeout
print("--- Setting Timeout ---")
try:
    response = requests.get(url, timeout=10)
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
