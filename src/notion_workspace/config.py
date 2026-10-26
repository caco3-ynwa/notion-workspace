import os
from pathlib import Path

from dotenv import load_dotenv

NOTION_TOKEN = ""
LOG_FILE = "logs/sync.log"


def load_config(env_path: str) -> None:
    global NOTION_TOKEN, LOG_FILE

    env_file = Path(env_path).expanduser().resolve()

    if not env_file.is_file():
        raise ValueError(f"配置文件不存在：{env_file}")

    load_dotenv(env_file, override=False)

    NOTION_TOKEN = os.getenv("NOTION_TOKEN", "")
    LOG_FILE = os.getenv("LOG_FILE", "logs/sync.log")

    if not NOTION_TOKEN:
        raise ValueError("请在配置文件或环境变量中设置 NOTION_TOKEN")
