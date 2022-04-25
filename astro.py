from pathlib import Path

import requests

Path("images").mkdir(parents=True, exist_ok=True)

filename = "hubble.jpeg"
url = "https://upload.wikimedia.org/wikipedia/commons/3/3f/HST-SM4.jpeg"

response = requests.get(url)
response.raise_for_status()

with open(f"images/{filename}", 'wb') as file:
    file.write(response.content)
