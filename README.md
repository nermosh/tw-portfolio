# Anastasiia Motovilova — Technical Writer Portfolio

A personal portfolio site built with [Zensical](https://zensical.org), hosted on GitHub Pages.

**Live site:** https://nermosh.github.io/tw-portfolio/

## About

This portfolio showcases projects from over ten years of work in Technical Writing, Knowledge Management, Instructional Design, and AI-assisted content strategy. Projects are organized by area of expertise, with each page covering goals, constraints, my role, and key achievements.

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
docs/          # Markdown source pages
site/          # Built static output (auto-generated, not edited manually)
source-files/  # Raw notes and drafts used as source material
zensical.toml  # Site configuration
```
