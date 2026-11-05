# next code
import requests
import pandas as pd
URL = "https://raw.githubusercontent.com/csmith651/Python-Projects-CIS-103-/refs/heads/main/anime_dataset.csv"
def fetch_user():
    try:
        response = requests.get(URL, timeout=10)
        response.raise_for_status()      # raises on 4xx / 5xx
        data = response.text             # get response body as text
        print(data)
    except requests.RequestException as error:
        print("Fetch error:", error)

fetch_user()

