import logging
from pathlib import Path

from notion_workspace.tasks import task_management

Path("logs").mkdir(exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler(
            "logs/sync.log",
            encoding="utf-8",
        ),
    ],
)


logger = logging.getLogger(__name__)

def main():
    logger.info("start notion workspace")
    task_management.run_tasks()




if __name__ == "__main__":
    main()