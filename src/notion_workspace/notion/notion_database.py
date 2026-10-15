from notion_workspace.notion.client import notion_client as client


class NotionDatabase:
    def __init__(self,  data_source_id: str):
        self.client = client
        self.data_source_id = data_source_id

    def existsTitle(self, property: str, title: str) -> bool:
        response = self.client.data_sources.query(
            data_source_id=self.data_source_id,
            filter={
                "property": property,
                "title": {"equals": title},
            },
            page_size=1,
        )

        return bool(response["results"])

    def create(self, properties: dict):
        return self.client.pages.create(
            parent={
                "type": "data_source_id",
                "data_source_id": self.data_source_id,
            },
            properties=properties,
        )

if __name__ == "__main__":
    database = NotionDatabase(
    data_source_id="38ebd80b-3ee0-80f1-8e99-000bcc29e8a4",)
    print(database.existsTitle("MatchId", "caco4"))
    print(database.existsTitle("MatchId", "caco3"))


