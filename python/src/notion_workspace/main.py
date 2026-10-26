import argparse
import logging
from pathlib import Path

from notion_workspace import config


def main():
    parser = argparse.ArgumentParser(description="Notion 同步程序")

    parser.add_argument(
        "--env-file",
        default=None,
        help=".env 文件路径，默认读取仓库根目录（打包后为可执行文件旁）的 .env",
    )

    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument(
        "--schedule",
        action="store_true",
        help="开启定时任务模式",
    )
    mode.add_argument(
        "--data-sync",
        choices=["sync_dota_records"],
        help="立即执行指定任务",
    )

    args = parser.parse_args()

    try:
        config.load_config(args.env_file)
    except ValueError as exc:
        parser.error(str(exc))

    log_file = Path(config.LOG_FILE).expanduser()
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
    logger.info("启动 Notion 同步程序")

    # 必须在加载配置之后导入，业务模块会初始化 Notion 客户端
    if args.schedule:
        from notion_workspace.tasks import task_management

        task_management.run_tasks()
    else:
        from notion_workspace.notion import data_sync

        data_sync.sync_dota_records(limit=10)


if __name__ == "__main__":
    main()