import argparse
import os
from pathlib import Path

from dotenv import load_dotenv

parser = argparse.ArgumentParser()
parser.add_argument(
    "--env-file",
    required=True,
    help=".env 文件路径",
)
args = parser.parse_args()

env_file = Path(args.env_file).expanduser().resolve()

if not env_file.is_file():
    parser.error(f"配置文件不存在：{env_file}")

load_dotenv(env_file, override=False)

NOTION_TOKEN = os.getenv("NOTION_TOKEN")

if not NOTION_TOKEN:
    parser.error("请在配置文件或环境变量中设置 NOTION_TOKEN")