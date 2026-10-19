from dotenv import load_dotenv
from notion_client import Client
import os
from datetime import datetime, timezone


print("Hello, World!")
success = load_dotenv()
print("load_dotenv:", success)

NOTION_TOKEN = os.getenv("NOTION_TOKEN")
print("NOTION_TOKEN:", NOTION_TOKEN)

notion = Client(auth=os.getenv("NOTION_TOKEN"))

DATABASE_ID = "38ebd80b3ee080c0b298d39b388de548"


database = notion.databases.retrieve(database_id=DATABASE_ID)

data_sources = database["data_sources"]

for ds in data_sources:
    print("name:", ds["name"])
    print("id:", ds["id"])

DATA_SOURCE_ID = data_sources[0]["id"]

response = notion.data_sources.query(data_source_id=DATA_SOURCE_ID)


result = notion.pages.create(
    parent={"data_source_id": DATA_SOURCE_ID},
    properties={
        "MatchId": {"title": [{"text": {"content": "New Page"}}]},
        "Date": {
            "date": {
                "start": datetime.now(timezone.utc).isoformat()
            }
        },
    },
)

print("Created page with ID:", result["id"])
print("DATA_SOURCE_ID:", DATA_SOURCE_ID)