# Anastasiia Motovilova — Technical Writer Portfolio

A personal portfolio site built with [Zensical](https://zensical.org), hosted on GitHub Pages.

**Live site:** https://nermosh.github.io/tw-portfolio/

## About

This portfolio showcases projects from over ten years of work in Technical Writing, Knowledge Management, Instructional Design, and AI-assisted content strategy. Each page covers goals, constraints, my role, and key achievements.

**Current pages:**

| Page | File | Description |
|---|---|---|
| About Me | `docs/index.md` | Background, specialization, toolkit, education |
| Knowledge Management | `docs/kb.md` | Enterprise-scale KB project at Intermedia Communications |
| Style Guide | `docs/style-guide.md` | Style guide work across two companies |

Individual project stories are managed through the CMS and published under their topic section. Additional pages (`api.md`, `how-to.md`, `l10n.md`, `learning.md`) are drafted but not yet enabled in navigation.

## Stack

- **Static site generator:** Zensical (Python-based, MkDocs-compatible)
- **CMS:** Decap CMS (local, Git-backed — no external service required)
- **Content:** Markdown with YAML frontmatter
- **Hosting:** GitHub Pages

## Project structure

```
docs/
  index.md              # About Me page (live)
  kb.md                 # Knowledge Management page (live)
  style-guide.md        # Style Guide page (live)
  *.md                  # Draft pages (not yet in navigation)
  images/               # Photos, diagrams, favicons, story images
  admin/
    index.html          # Decap CMS UI (loaded from CDN)
    config.yml          # CMS content model — collections, fields, slugs
  engagements/          # CMS data: one file per role/company phase
  stories/              # CMS data: one file per project story
  stories-rendered/     # Auto-generated — do not edit by hand (git-ignored)
  stylesheets/
    extra.css           # Custom styles
scripts/
  render_stories.py     # Generates stories-rendered/ from stories/ + engagements/
  start-cms.sh          # Helper: starts the local CMS server
  build.sh              # Helper: renders stories and builds the site
hooks/
  story_formatter.py    # MkDocs hook scaffold (currently unused — Zensical limitation)
source-files/           # Raw notes and drafts used as source material (git-ignored)
site/                   # Built static output — auto-generated (git-ignored)
zensical.toml           # Site configuration and navigation
```

## Daily workflow

### First-time setup

**Requirements:** Python 3.x, Node.js LTS

```bash
# Create and activate a virtual environment
python -m venv venv
source venv/Scripts/activate    # Windows (Git Bash)
source venv/bin/activate        # macOS / Linux

# Install Python dependencies
pip install zensical

# Install Node.js dependencies (first run only)
npm install
```

### Editing content in the CMS

```bash
bash scripts/start-cms.sh
```

Opens the CMS at `http://localhost:8000/admin/`. Both the Decap Git proxy (port 8081) and the static file server (port 8000) run in the same terminal. Press `Ctrl+C` to stop both.

### Building and previewing the site

After saving changes in the CMS:

```bash
bash scripts/build.sh
```

This renders all stories from their CMS source files and builds the static site.

To preview with live reload instead of a one-time build:

```bash
source venv/Scripts/activate
zensical serve
```

### Publishing

Push to the `main` branch. GitHub Actions builds and deploys to GitHub Pages automatically.

## How stories work

Stories are stored as structured data in `docs/stories/` (one `.md` file per story, with YAML frontmatter). Each story links to an **engagement** in `docs/engagements/` — one engagement per company/role phase.

The `scripts/render_stories.py` script reads both collections, injects consistent section headings with icons, and writes the final pages to `docs/stories-rendered/`. The site nav points to the rendered files.

**Do not edit files in `docs/stories-rendered/` directly** — they are overwritten on every build.
