"""
Pre-build script: reads docs/stories/*.md (CMS data files), assembles full
formatted pages, and writes them to docs/stories-rendered/.

Run before `zensical serve` or `zensical build`.
"""

import re
import shutil
import yaml
from pathlib import Path

STORIES_DIR = Path("docs/stories")
ENGAGEMENTS_DIR = Path("docs/engagements")
OUTPUT_DIR = Path("docs/stories-rendered")
TOML_PATH = Path("zensical.toml")

# Fixed nav shape: (section label, static page, story section key or None)
NAV_STRUCTURE = [
    ("About Me",             "index.md",       None),
    ("Knowledge Management", "kb.md",          "Knowledge Management"),
    ("Style Guide",          "style-guide.md", "Style Guide"),
]
NAV_COMMENTED = [
    '#{ "Document Types" = "how-to.md"}',
    '#{ "API Documents" = "api.md" }',
    '#{ "Localization" = "l10n.md"}',
    '#{ "Training" = "learning.md"}',
]

CONTEXT_FIELDS = [
    ("company_size",  ":lucide-building-2:",  "Company Size"),
    ("role",          ":lucide-briefcase:",    "Role"),
    ("period",        ":lucide-calendar:",     "Period"),
    ("team_scale",    ":lucide-users:",        "Team"),
    ("toolkit",       ":lucide-pen-tool:",     "Toolkit"),
    ("library_scale", ":lucide-library-big:",  "Library Scale"),
]

STORY_SECTIONS_BEFORE_CONTEXT = [
    ("goal",  "## :lucide-target: Goal"),
    ("role",  "## :lucide-user-check: My Role"),
]

STORY_SECTIONS_AFTER_CONTEXT = [
    ("constraints",  "## :lucide-triangle-alert: Constraints"),
    ("obstacles",    "## :lucide-construction: Obstacles"),
]

LESSONS_HEADING = "## :lucide-book-open-check: Lessons Learned"


def parse_file(path: Path) -> tuple[dict, str]:
    raw = path.read_text(encoding="utf-8")
    match = re.match(r"^---\n(.*?)\n---\n?(.*)", raw, re.DOTALL)
    if not match:
        return {}, raw.strip()
    return yaml.safe_load(match.group(1)) or {}, match.group(2).strip()


def build_context_lines(eng_meta: dict) -> str:
    lines = []
    for field, icon, label in CONTEXT_FIELDS:
        value = eng_meta.get(field)
        if not value:
            continue
        if isinstance(value, list):
            value = ", ".join(str(v) for v in value)
        lines.append(f"{icon} **{label}:** {value}")
    return "\n\n".join(lines)


def render_story(story_path: Path) -> str:
    meta, body = parse_file(story_path)

    # ── Context block ────────────────────────────────────────────────────────
    eng_meta, eng_body = {}, ""
    engagement_slug = meta.get("engagement")
    if engagement_slug:
        eng_path = ENGAGEMENTS_DIR / f"{engagement_slug}.md"
        if eng_path.exists():
            eng_meta, eng_body = parse_file(eng_path)

    context_lines = build_context_lines(eng_meta)
    context_content = context_lines
    if eng_body:
        context_content = f"{context_lines}\n\n{eng_body}" if context_lines else eng_body

    # ── Image ────────────────────────────────────────────────────────────────
    image = meta.get("image", "").strip()

    # ── Assemble sections: Goal → My Role → Context → Constraints → … ───────
    parts = []

    for field, heading in STORY_SECTIONS_BEFORE_CONTEXT:
        value = meta.get(field, "").strip()
        if value:
            parts.append(f"{heading}\n\n{value}")

    if image:
        parts.append(
            '<div class="story-header" markdown="1">\n'
            '<div class="story-context" markdown="1">\n\n'
            f"## :lucide-building-2: Context\n\n{context_content}\n\n"
            '</div>\n'
            '<div class="story-image" markdown="1">\n\n'
            f"![Story image]({image})\n\n"
            '</div>\n'
            '</div>'
        )
    elif context_content:
        parts.append(f"## :lucide-building-2: Context\n\n{context_content}")

    for field, heading in STORY_SECTIONS_AFTER_CONTEXT:
        value = meta.get(field, "").strip()
        if value:
            parts.append(f"{heading}\n\n{value}")

    if body:
        parts.append(body)

    lessons = meta.get("lessons", "").strip()
    if lessons:
        parts.append(f"{LESSONS_HEADING}\n\n{lessons}")

    title = meta.get("title", story_path.stem.replace("-", " ").title())
    frontmatter = f"---\ntitle: {title}\n---\n\n"
    return frontmatter + "\n\n".join(parts)


def build_nav_block(story_sections: dict) -> str:
    entries = []
    for label, static_page, section_key in NAV_STRUCTURE:
        stories = story_sections.get(section_key, []) if section_key else []
        all_pages = ([static_page] if static_page else []) + [f"stories-rendered/{s}" for s in stories]
        if not all_pages:
            continue
        if len(all_pages) == 1:
            entries.append(f'    {{ "{label}" = "{all_pages[0]}" }}')
        else:
            inner = "\n".join(f'        "{p}",' for p in all_pages[:-1])
            inner += f'\n        "{all_pages[-1]}"'
            entries.append(f'    {{ "{label}" = [\n{inner}\n    ]}}')

    body = ",\n".join(entries)
    if NAV_COMMENTED:
        body += ",\n" + "\n".join(f"    {c}" for c in NAV_COMMENTED)
    return f"nav = [\n{body}\n]"


def update_nav(story_sections: dict) -> None:
    content = TOML_PATH.read_text(encoding="utf-8")
    new_nav = build_nav_block(story_sections)
    updated = re.sub(r"nav = \[[\s\S]*?\n\]", new_nav, content)
    TOML_PATH.write_text(updated, encoding="utf-8")
    print(f"  updated: {TOML_PATH} (nav)")


def main():
    if OUTPUT_DIR.exists():
        shutil.rmtree(OUTPUT_DIR)
    OUTPUT_DIR.mkdir(parents=True)

    stories = list(STORIES_DIR.glob("*.md"))
    if not stories:
        print("No stories found.")
        return

    story_sections: dict[str, list[tuple[int, str]]] = {}

    for story_path in stories:
        meta, _ = parse_file(story_path)
        rendered = render_story(story_path)
        out_path = OUTPUT_DIR / story_path.name
        out_path.write_text(rendered, encoding="utf-8")
        print(f"  rendered: {out_path}")

        section = meta.get("section")
        if section:
            year_raw = str(meta.get("year", "0"))[:4]
            year = int(year_raw) if year_raw.isdigit() else 0
            story_sections.setdefault(section, []).append((year, story_path.name))

    sorted_sections = {
        section: [name for _, name in sorted(entries, reverse=True)]
        for section, entries in story_sections.items()
    }
    update_nav(sorted_sections)

    print(f"Done — {len(stories)} story/stories written to {OUTPUT_DIR}/")


if __name__ == "__main__":
    main()
