#!/bin/bash
# Renders story pages from CMS data and builds the static site.
# Run this after saving changes in the CMS, before pushing to GitHub.

source venv/Scripts/activate

echo "Rendering stories..."
python scripts/render_stories.py || exit 1

echo "Building site..."
zensical build

echo ""
echo "Done. Preview with: source venv/Scripts/activate && zensical serve"
