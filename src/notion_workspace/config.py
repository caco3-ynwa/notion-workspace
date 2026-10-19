import os
import sys
from pathlib import Path

from dotenv import load_dotenv

if getattr(sys, "frozen", False):
    # 打包后：可执行文件所在目录
    base_dir = Path(sys.executable).resolve().parent
else:
    # 开发时：项目根目录
    base_dir = Path(__file__).resolve().parents[2]

load_dotenv(base_dir / ".env", override=False)

NOTION_TOKEN = os.getenv("NOTION_TOKEN")

if not NOTION_TOKEN:
    raise RuntimeError("请在 .env 或环境变量中配置 NOTION_TOKEN")