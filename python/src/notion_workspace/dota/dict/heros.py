from pathlib import Path

import pandas as pd


class HeroMap:
    def __init__(self):
        csv_path = Path(__file__).resolve().parent / "heroes.csv"

        df = pd.read_csv(csv_path)

        self.heroes = dict(
            zip(df["id"], df["localized_name"])
        )

    def get_name(self, hero_id: int) -> str:
        return self.heroes.get(hero_id, "Unknown")


hero_map = HeroMap()