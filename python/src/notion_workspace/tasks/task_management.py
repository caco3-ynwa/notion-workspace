from notion_workspace.tasks import dota_record_sync_task

TASKS = [dota_record_sync_task]

def run_tasks():
    for task in TASKS:
        task.run()


if __name__ == "__main__":
    run_tasks()
