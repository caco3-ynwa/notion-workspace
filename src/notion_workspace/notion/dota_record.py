from dataclasses import dataclass
from typing import Protocol

from notion_workspace.notion.constants import DatabaseSchema, Property, PropertyType
from notion_workspace.notion.notion_database import NotionDatabase

DOTA_RECORD_DATABASE_ID = "38ebd80b3ee080c0b298d39b388de548"

# win_encoder = lambda win: "win" if win else "lose"
data_source_id = "38ebd80b-3ee0-80f1-8e99-000bcc29e8a4"

MATCH_SCHEMA = DatabaseSchema(
    name="recordes",
    properties=(
        Property("recordId", PropertyType.TITLE, "record_id", primary=True),
        Property("Hero", PropertyType.RICH_TEXT, "hero_name"),
        Property("HeroId", PropertyType.NUMBER, "hero_id"),
        Property("Kills", PropertyType.NUMBER, "kills"),
        Property("Deaths", PropertyType.NUMBER, "deaths"),
        Property("Assists", PropertyType.NUMBER, "assists"),
        Property("Win/Lose", PropertyType.SELECT, "win"),
        Property("Date", PropertyType.DATE, "date"),
    ),
)


@dataclass(frozen=True)
class DotaRecord(Protocol):
    record_id: int
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
    if notion.existsTitle("recordId", str(record.match_id)):
        print(f"Skipped: {record.record_id}")

    properties = MATCH_SCHEMA.encode_object(record)

    notion.create(properties)

    print(f"Created: {record.match_id}")


if __name__ == "__main__":
    print(record_SCHEMA.to_notion_schema())
