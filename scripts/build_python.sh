#!/usr/bin/env bash
set -euo pipefail
PROJECT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$PROJECT_DIR"

# Reuse the ECS Conda installation when present; otherwise use active Python.
CONDA_SH="${CONDA_SH:-$HOME/miniconda-24/etc/profile.d/conda.sh}"
if [[ -f "$CONDA_SH" ]]; then
    source "$CONDA_SH"
    conda activate "${CONDA_ENV_NAME:-notion}"
fi
PYTHON_BIN="${PYTHON_BIN:-python}"
"$PYTHON_BIN" -m PyInstaller \
    --noconfirm --onefile --name notion-sync \
    --paths "$PROJECT_DIR/python/src" \
    --add-data "$PROJECT_DIR/python/src/notion_workspace/dota/dict/heroes.csv:notion_workspace/dota/dict" \
    --collect-data tzdata \
    --distpath "$PROJECT_DIR/dist/python" \
    --workpath "$PROJECT_DIR/build/python/work" \
    --specpath "$PROJECT_DIR/build/python" \
    "$PROJECT_DIR/python/src/notion_workspace/main.py"
printf 'Built: %s/dist/python/notion-sync\n' "$PROJECT_DIR"
