from notion_workspace.dota import opendota
from notion_workspace.notion.dota_record import MATCH_SCHEMA
from notion_workspace.notion.notion_database import NotionDatabase


def main():
    limit = 5
    data_source_id="38ebd80b-3ee0-80f1-8e99-000bcc29e8a4"
    notion = NotionDatabase(
        data_source_id=data_source_id,
    )

    matches = opendota.recent_matches(opendota.account_id,limit)

    for match in matches:
        print(match)
        if notion.existsTitle("MatchId", str(match.match_id)):
            print(f"Skipped: {match.match_id}")
            continue

        properties = MATCH_SCHEMA.encode_object(match)

        notion.create(properties)

        print(f"Created: {match.match_id}")



if __name__ == "__main__":
    main()