from notion_workspace.dota import opendota
from notion_workspace.notion.dota_record import create_dota_record


def sync_dota_records(limit = 5):
    limit = 5
    matches = opendota.recent_matches(opendota.account_id,limit)

    for match in matches:
        create_dota_record(match)


if __name__ == "__main__":
    sync_dota_records(limit=5)
