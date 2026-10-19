from dataclasses import dataclass
from typing import Protocol

from notion_workspace.notion.constants import DatabaseSchema, Property, PropertyType
from notion_workspace.notion.notion_database import NotionDatabase

DOTA_RECORD_DATABASE_ID = "38ebd80b3ee080c0b298d39b388de548"

# win_encoder = lambda win: "win" if win else "lose"
data_source_id = "3fabd80b-3ee0-8095-b26d-000be5cb3b4d"

MATCH_SCHEMA = DatabaseSchema(
    name="recordes",
    properties=(
        Property("TaskId", PropertyType.TITLE, "task_id", primary=True),
        Property("Type", PropertyType.SELECT, "type"),
        Property("Status", PropertyType.SELECT, "status"),
        Property("StartTime", PropertyType.DATE, "start_time"),
        Property("EndTime", PropertyType.DATE, "end_time"),
    ),
)


@dataclass(frozen=True)
class DotaRecord(Protocol):
    match_id: int
    hero_id: int
    hero_name: str
    kills: int
    deaths: int
    assists: int
    player_slot: int
    radiant_win: bool
    start_time: int
    date: str
    win: bool


def create_dota_record(record: DotaRecord):
    notion = NotionDatabase(
        data_source_id=data_source_id,
    )

    print(record)
    if notion.existsTitle("MatchId", str(record.match_id)):
        print(f"Skipped: {record.match_id}")

    properties = MATCH_SCHEMA.encode_object(record)

    notion.create(properties)

    print(f"Created: {record.match_id}")


if __name__ == "__main__":
    print(MATCH_SCHEMA.to_notion_schema())
