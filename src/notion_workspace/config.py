from dotenv import load_dotenv
import os

success = load_dotenv()
print("load_dotenv:", success)

NOTION_TOKEN = os.getenv("NOTION_TOKEN")
print(f"NOTION_TOKEN: {NOTION_TOKEN}")
