#!/usr/bin/env bash
set -euo pipefail
PROJECT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$PROJECT_DIR"
ENV_FILE="${1:-$PROJECT_DIR/.env}"
exec "${NOTION_SYNC_BIN:-/usr/local/bin/notion-sync}" --env-file "$ENV_FILE" --data-sync sync_dota_records
