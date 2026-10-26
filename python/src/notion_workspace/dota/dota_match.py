from dataclasses import dataclass
from datetime import UTC, datetime

from notion_workspace.dota.dict.heros import hero_map


@dataclass(frozen=True)
class DotaMatch:
    match_id: int
    hero_id: int
    kills: int
    deaths: int
    assists: int
    player_slot: int
    radiant_win: bool
    start_time: int

    @property
    def hero_name(self) -> str:
        return hero_map.get_name(self.hero_id)


    @property
    def win(self) -> bool:
        is_radiant = self.player_slot < 128
        return self.radiant_win == is_radiant

    @property
    def date(self) -> str:
        return datetime.fromtimestamp(
            self.start_time,
            tz=UTC,
        ).isoformat()

    @classmethod
    def from_api(cls, data: dict) -> "DotaMatch":
        return cls(
            match_id=data["match_id"],
            hero_id=data["hero_id"],
            kills=data["kills"],
            deaths=data["deaths"],
            assists=data["assists"],
            player_slot=data["player_slot"],
            radiant_win=data["radiant_win"],
            start_time=data["start_time"],
        )
