import pandas as pd
import requests

url = "https://api.opendota.com/api/heroes"

response = requests.get(url, timeout=10)
response.raise_for_status()

heroes = response.json()

df = pd.DataFrame(heroes)

df.to_csv(
    "heroes.csv",
    index=False,
    encoding="utf-8-sig",
)