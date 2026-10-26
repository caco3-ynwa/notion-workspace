#!/usr/bin/env bash
set -euo pipefail
PROJECT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")/.." && pwd)"
bash "$PROJECT_DIR/scripts/build_python.sh"
install -m 755 "$PROJECT_DIR/dist/python/notion-sync" /usr/local/bin/notion-sync
