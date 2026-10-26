#!/usr/bin/env bash
set -euo pipefail
PROJECT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$PROJECT_DIR"
ENV_FILE="${1:-$PROJECT_DIR/.env}"
exec "$PROJECT_DIR/dist/python/notion-sync" --env-file "$ENV_FILE" --schedule
