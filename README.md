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

Additional pages (`api.md`, `how-to.md`, `l10n.md`, `learning.md`) are drafted but not yet enabled in navigation.

## Stack

- **Static site generator:** Zensical (Python-based, MkDocs-compatible)
- **Content:** Markdown
- **Hosting:** GitHub Pages

## Local development

**Requirements:** Python 3.x

```bash
# Create and activate a virtual environment
python -m venv venv
venv\Scripts\activate       # Windows
source venv/bin/activate    # macOS / Linux

# Install dependencies
pip install zensical

# Serve locally with live reload
python -m zensical serve

# Build static output
python -m zensical build
```

The site will be available at `http://localhost:8000`.

## Project structure

```
docs/             # Markdown source pages
  index.md        # About Me (live)
  kb.md           # Knowledge Management (live)
  style-guide.md  # Style Guide (live)
  *.md            # Draft pages (not yet in navigation)
  images/         # Photos, diagrams, favicons
site/             # Built static output — auto-generated, git-ignored
source-files/     # Raw notes and drafts used as source material
zensical.toml     # Site configuration and navigation
```
