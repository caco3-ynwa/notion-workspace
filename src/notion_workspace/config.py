import os
import sys
from pathlib import Path

from dotenv import load_dotenv

NOTION_TOKEN = ""
LOG_FILE = "logs/sync.log"


def load_config(env_path: str | None = None) -> None:
    global NOTION_TOKEN, LOG_FILE

    if env_path is not None:
        env_file = Path(env_path).expanduser().resolve()
    elif getattr(sys, "frozen", False):
        # 打包后默认读取可执行文件旁边的 .env
        env_file = Path(sys.executable).resolve().parent / ".env"
    else:
        # config.py 位于 src/notion_workspace/ 下
        env_file = Path(__file__).resolve().parents[2] / ".env"

    if not env_file.is_file():
        raise ValueError(f"配置文件不存在：{env_file}")

    load_dotenv(env_file, override=False)

    NOTION_TOKEN = os.getenv("NOTION_TOKEN", "")
    LOG_FILE = os.getenv("LOG_FILE", "logs/sync.log")

    if not NOTION_TOKEN:
        raise ValueError("请在配置文件或环境变量中设置 NOTION_TOKEN")


# 导入时加载默认配置；默认文件不存在则跳过，
# 允许 main.py 随后通过 --env-file 指定文件。
if getattr(sys, "frozen", False):
    default_env = Path(sys.executable).resolve().parent / ".env"
else:
    default_env = Path(__file__).resolve().parents[2] / ".env"

if default_env.is_file():
    load_config(str(default_env))
else:
    NOTION_TOKEN = os.getenv("NOTION_TOKEN", "")
    LOG_FILE = os.getenv("LOG_FILE", "logs/sync.log")