import argparse
import logging
from pathlib import Path

from notion_workspace.notion import data_sync
from notion_workspace.config import LOG_FILE
from notion_workspace.tasks import task_management

log_file = Path(LOG_FILE).expanduser()
log_file.parent.mkdir(parents=True, exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler(log_file, encoding="utf-8"),
    ],
    force=True,
)

logger = logging.getLogger(__name__)
parser = argparse.ArgumentParser(description="Notion 同步程序")
parser.add_argument(
    "--schedule",
    action="store_true",
    help="开启定时任务模式",
)
parser.add_argument(
    "--data-sync",
    type=str,
    help="执行指定的任务",
)



def main():
    logger.info("start notion workspace")
    if parser.parse_args().schedule:
        logger.info("Running in schedule mode...")
        task_management.run_tasks()
        return

    if parser.parse_args().data_sync:
        task_name = parser.parse_args().data_sync
        if task_name == "sync_dota_records":
            logger.info("Running sync_dota_records task...")
            data_sync.sync_dota_records(limit=10)
        else:
            logger.error(f"Unknown task: {task_name}")






if __name__ == "__main__":
    main()