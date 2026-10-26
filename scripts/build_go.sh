#!/usr/bin/env bash
set -euo pipefail
PROJECT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$PROJECT_DIR/go"
if [[ ! -f cmd/notion-sync/main.go ]]; then
    printf '%s\n' 'Go entry point is not implemented yet: go/cmd/notion-sync/main.go' >&2
    exit 1
fi
mkdir -p "$PROJECT_DIR/dist/go"
go build -o "$PROJECT_DIR/dist/go/notion-sync" ./cmd/notion-sync
