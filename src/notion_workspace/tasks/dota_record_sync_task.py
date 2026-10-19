import logging

from apscheduler.schedulers.blocking import BlockingScheduler

from notion_workspace.notion.data_sync import sync_dota_records

logging.basicConfig(level=logging.INFO)


def sync_job():
    sync_dota_records(limit = 10)
    # 调用之前带 Notion 日志记录的函数


def run():
    scheduler = BlockingScheduler(timezone="Asia/Shanghai")

    scheduler.add_job(
        sync_job,
        trigger="cron",
        hour=16,
        minute=14,
        max_instances=1,
        coalesce=True,
        misfire_grace_time=300,
    )
    scheduler.start()

if __name__ == "__main__":
    try:
        print("Starting the scheduler...")
        run()
    except (KeyboardInterrupt, SystemExit):
        pass