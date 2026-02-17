#!/bin/bash
# Sync raw HTML from wiki-static server into _raw/ staging directory.
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
DEST="$SCRIPT_DIR/../_raw"
mkdir -p "$DEST"

for wiki in python psf jython; do
    echo "Syncing $wiki..."
    rsync -avz --delete \
        --include='*.html' \
        --include='attachments/***' \
        --include='logo.png' \
        --exclude='europython/' \
        --exclude='pagefind/' \
        "coffee@wiki:/data/www/wiki-static/$wiki/" \
        "$DEST/$wiki/"
done

echo "Done. Raw HTML synced to $DEST"
