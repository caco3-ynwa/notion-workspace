import requests
import pandas as pd
from constants import ACCOUNT_ID

account_id = ACCOUNT_ID
try:
    url = f"https://api.opendota.com/api/players/{account_id}/matches"
    response = requests.get(url,
                            timeout=10)
    response.raise_for_status()

    data = response.json()
    print(data)
    
except requests.exceptions.Timeout:
    print("OpenDota API 请求超时")

except requests.exceptions.RequestException as e:
    print("OpenDota API 请求失败:", e)


df = pd.DataFrame(data)
print(df.head())

print(df)
