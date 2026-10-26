from urllib import response

import requests

from notion_workspace.dota.constants import ACCOUNT_ID
from notion_workspace.dota.dota_match import DotaMatch

account_id = ACCOUNT_ID

BASE_URL = "https://api.opendota.com/api/"


def recent_matches(account_id, limit=10):
    url = f"{BASE_URL}players/{account_id}/recentMatches?limit={limit}"
    match_data = request_opendota(url)
    return [DotaMatch.from_api(data) for data in match_data]


def request_opendota(url):
    try:
        response = requests.get(url, timeout=10)
        print(response.status_code)
        print(response.text)
        response.raise_for_status()
        return response.json()

        # data = response.json()
        # df = pd.DataFrame(data)
        # print(df.head())
        # print(df)
    except requests.exceptions.Timeout:
        print("OpenDota API 请求超时")
    except requests.exceptions.RequestException as e:
        print("OpenDota API 请求失败:", e)


if __name__ == "__main__":
    matches = recent_matches(account_id, limit=5)
    for match in matches:
        print(match)
