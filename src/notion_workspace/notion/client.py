import json

from notion_client import Client

from notion_workspace.config import NOTION_TOKEN

notion_client = Client(auth=NOTION_TOKEN)
# def notion_database_oper(datasource_id:str):
    

page_id = "3b2bd80b3ee0812da52bff65597fa178?"

page = notion_client.pages.retrieve(page_id=page_id)

# print(json.dumps(page, indent=2))
title = page["properties"]["title"]["title"][0]["plain_text"]
# print(f"Page title: {title}")
