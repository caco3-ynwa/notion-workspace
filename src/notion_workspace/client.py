from notion_client import Client
from config import NOTION_TOKEN
import json

notion = Client(auth=NOTION_TOKEN)

page_id = "3b2bd80b3ee0812da52bff65597fa178?"

page = notion.pages.retrieve(page_id=page_id)

print(json.dumps(page, indent=2))
title = page["properties"]["title"]["title"][0]["plain_text"]
print(f"Page title: {title}")
