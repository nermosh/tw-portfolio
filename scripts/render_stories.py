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

CONTEXT_FIELDS = [
    ("company",       ":lucide-building-2:",  "Company"),
    ("role",          ":lucide-briefcase:",    "Role"),
    ("period",        ":lucide-calendar:",     "Period"),
    ("team_scale",    ":lucide-users:",        "Team"),
    ("toolkit",       ":lucide-pen-tool:",     "Toolkit"),
    ("library_scale", ":lucide-library-big:",  "Library Scale"),
]

STORY_SECTIONS = [
    ("goal",         "## :lucide-target: Goal"),
    ("role",         "## :lucide-user-check: My Role"),
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

    # ── Assemble sections ────────────────────────────────────────────────────
    parts = []

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

    for field, heading in STORY_SECTIONS:
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


def main():
    if OUTPUT_DIR.exists():
        shutil.rmtree(OUTPUT_DIR)
    OUTPUT_DIR.mkdir(parents=True)

    stories = list(STORIES_DIR.glob("*.md"))
    if not stories:
        print("No stories found.")
        return

    for story_path in stories:
        rendered = render_story(story_path)
        out_path = OUTPUT_DIR / story_path.name
        out_path.write_text(rendered, encoding="utf-8")
        print(f"  rendered: {out_path}")

    print(f"Done — {len(stories)} story/stories written to {OUTPUT_DIR}/")


if __name__ == "__main__":
    main()
