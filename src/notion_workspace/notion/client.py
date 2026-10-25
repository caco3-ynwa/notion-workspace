import json

from notion_client import Client

from notion_workspace import config



if not config.NOTION_TOKEN:
    raise RuntimeError("请先调用 config.load_config() 加载配置")
notion_client = Client(auth=config.NOTION_TOKEN)
# def notion_database_oper(datasource_id:str):
    

# page_id = "3b2bd80b3ee0812da52bff65597fa178?"

# page = notion_client.pages.retrieve(page_id=page_id)

# print(json.dumps(page, indent=2))
# title = page["properties"]["title"]["title"][0]["plain_text"]
# print(f"Page title: {title}")
