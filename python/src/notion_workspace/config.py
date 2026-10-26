import os
import sys
from pathlib import Path

from dotenv import dotenv_values


def default_env_path() -> Path:
    if getattr(sys, "frozen", False):
        return Path(sys.executable).resolve().parent / ".env"
    # Repository root: python/src/notion_workspace/config.py
    return Path(__file__).resolve().parents[3] / ".env"


NOTION_TOKEN = ""
LOG_FILE = "logs/sync.log"


def _apply_config(env_file: Path) -> None:
    global NOTION_TOKEN, LOG_FILE
    # Do not insert defaults into os.environ: an explicit file must be
    # able to replace an automatically loaded default configuration.
    values = dotenv_values(env_file)
    NOTION_TOKEN = os.getenv("NOTION_TOKEN", values.get("NOTION_TOKEN") or "")
    LOG_FILE = os.getenv("LOG_FILE", values.get("LOG_FILE") or "logs/sync.log")


def load_config(env_path: str | None = None) -> None:
    env_file = (
        Path(env_path).expanduser().resolve()
        if env_path is not None else default_env_path()
    )
    if not env_file.is_file():
        raise ValueError(f"配置文件不存在：{env_file}")
    _apply_config(env_file)
    if not NOTION_TOKEN:
        raise ValueError("请在配置文件或环境变量中设置 NOTION_TOKEN")


# Support direct imports in local helper modules without parsing CLI arguments.
_default_env = default_env_path()
if _default_env.is_file():
    _apply_config(_default_env)
else:
    NOTION_TOKEN = os.getenv("NOTION_TOKEN", "")
    LOG_FILE = os.getenv("LOG_FILE", "logs/sync.log")
