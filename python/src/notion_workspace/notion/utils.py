from dotenv import load_dotenv
from notion_client import Client
import os
from datetime import datetime, timezone


success = load_dotenv()

NOTION_TOKEN = os.getenv("NOTION_TOKEN")

notion = Client(auth=os.getenv("NOTION_TOKEN"))

DATABASE_ID = "38ebd80b3ee080c0b298d39b388de548"

def get_datasouce_id(database_id):
    database = notion.databases.retrieve(database_id=database_id)
    data_sources = database["data_sources"]
    if not data_sources:
        raise ValueError("No data sources found in the database.")
    return data_sources[0]["id"]



def get_multi_datasouce_id(database_id):
    database = notion.databases.retrieve(database_id=database_id)
    data_sources = database["data_sources"]
    if not data_sources:
        raise ValueError("No data sources found in the database.")
    return [ds["id"] for ds in data_sources]