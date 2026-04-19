import re
import yaml
from pathlib import Path


def on_page_markdown(markdown, page, config, **kwargs):
    if not page.file.src_path.startswith("stories/"):
        return markdown

    src_path = Path(page.file.abs_src_path)
    raw = src_path.read_text(encoding="utf-8")
    match = re.match(r"^---\n(.*?)\n---\n?(.*)", raw, re.DOTALL)
    if not match:
        return markdown

    meta = yaml.safe_load(match.group(1)) or {}
    docs_dir = Path(config["docs_dir"])
    sections = []

    engagement_slug = meta.get("engagement")
    if engagement_slug:
        eng_path = docs_dir / "engagements" / f"{engagement_slug}.md"
        if eng_path.exists():
            context_block = _build_context(eng_path)
            if context_block:
                sections.append(f"## :lucide-building-2: Context\n\n{context_block}")

    if meta.get("goal"):
        sections.append(f"## :lucide-target: Goal\n\n{meta['goal']}")

    if meta.get("role"):
        sections.append(f"## :lucide-user-check: My Role\n\n{meta['role']}")

    toolkit = meta.get("toolkit")
    if toolkit:
        toolkit_md = "\n".join(f"- {t}" for t in toolkit) if isinstance(toolkit, list) else str(toolkit)
        sections.append(f"## :lucide-pen-tool: Toolkit\n\n{toolkit_md}")

    if meta.get("library_scale"):
        sections.append(f"## :lucide-library-big: Library Scale\n\n{meta['library_scale']}")

    if meta.get("constraints"):
        sections.append(f"## :lucide-triangle-alert: Constraints\n\n{meta['constraints']}")

    if meta.get("obstacles"):
        sections.append(f"## :lucide-construction: Obstacles\n\n{meta['obstacles']}")

    injected = "\n\n".join(sections)
    lessons = meta.get("lessons", "")

    if lessons:
        return f"{injected}\n\n{markdown}\n\n## :lucide-book-open-check: Lessons Learned\n\n{lessons}"
    return f"{injected}\n\n{markdown}"


def _build_context(eng_path: Path) -> str:
    raw = eng_path.read_text(encoding="utf-8")
    match = re.match(r"^---\n(.*?)\n---\n?(.*)", raw, re.DOTALL)
    if not match:
        return ""

    fm = yaml.safe_load(match.group(1)) or {}
    body = match.group(2).strip()

    lines = []
    if fm.get("company"):
        lines.append(f"**Company:** {fm['company']}")
    if fm.get("role"):
        lines.append(f"**Role:** {fm['role']}")
    if fm.get("period"):
        lines.append(f"**Period:** {fm['period']}")
    if fm.get("team_scale"):
        lines.append(f"**Team:** {fm['team_scale']}")

    result = "\n\n".join(lines)
    if body:
        result = f"{result}\n\n{body}" if result else body
    return result
