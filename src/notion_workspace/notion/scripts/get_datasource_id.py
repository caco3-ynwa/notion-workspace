from notion_workspace.notion.utils import get_datasouce_id


def main():
    database_id = "3fabd80b3ee080f0b032c152d101b4df"
    data_source_id = get_datasouce_id(database_id)
    print(f"Data Source ID: {data_source_id}")

if __name__ == "__main__":
    main()