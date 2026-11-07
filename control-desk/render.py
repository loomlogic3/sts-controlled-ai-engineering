#!/usr/bin/env python3
"""Render the file-based Control Desk as a read-only HTML document."""

from __future__ import annotations

import html
import json
import re
import sqlite3
import argparse
from pathlib import Path


ROOT = Path(__file__).resolve().parent
REGISTRY = ROOT / "projects.json"
RECORD_DIRS = ("milestones", "approvals", "risks", "verifications", "evidence", "decisions", "checkpoints")


def metadata_text(raw: str) -> tuple[dict[str, str], str]:
    lines = raw.splitlines()
    if not lines or lines[0].strip() != "---":
        return {}, "\n".join(lines)
    try:
        end = lines.index("---", 1)
    except ValueError:
        return {}, "\n".join(lines)
    values: dict[str, str] = {}
    for line in lines[1:end]:
        match = re.match(r"^([A-Za-z_][A-Za-z0-9_]*):\s*(.*)$", line)
        if match:
            values[match.group(1)] = match.group(2).strip()
    return values, "\n".join(lines[end + 1:]).strip()


def metadata(path: Path) -> tuple[dict[str, str], str]:
    return metadata_text(path.read_text(encoding="utf-8"))


def project_roots() -> dict[str, tuple[str, Path]]:
    registry = json.loads(REGISTRY.read_text(encoding="utf-8"))
    result = {}
    for project in registry.get("projects", []):
        project_id = project.get("project_id")
        if not project_id or not project.get("enabled", True):
            continue
        repository = (ROOT / project["repository_path"]).resolve()
        result[project_id] = (project.get("display_name", project_id), repository / "control-desk")
    return result


def records(database: Path | None = None) -> list[tuple[Path, dict[str, str], str]]:
    result = []
    if database is not None:
        with sqlite3.connect(database) as connection:
            rows = connection.execute(
                "SELECT project_id, source_path, raw_markdown FROM records WHERE active = 1 ORDER BY project_id, record_id"
            ).fetchall()
        for project_id, source_path, raw_markdown in rows:
            values, body = metadata_text(raw_markdown)
            if values:
                values.setdefault("project_id", project_id)
                result.append((Path(source_path), values, body))
        return result
    for project_id, (_, control_desk) in project_roots().items():
        for directory in RECORD_DIRS:
            folder = control_desk / directory
            if folder.exists():
                for path in sorted(folder.glob("*.md")):
                    values, body = metadata(path)
                    if values:
                        values.setdefault("project_id", project_id)
                        result.append((path, values, body))
    return result


def inline_markdown(text: str) -> str:
    """Render a safe subset of inline Markdown."""
    from urllib.parse import urlsplit

    pattern = re.compile(
        r"(`[^`]+`|\[[^]]+\]\((?:[^()]|\([^()]*\))+\)|\*\*.+?\*\*|__.+?__|~~.+?~~|\*[^*]+\*|_[^_]+_)"
    )
    output: list[str] = []
    position = 0

    for match in pattern.finditer(text):
        output.append(html.escape(text[position:match.start()]))
        token = match.group(0)

        if token.startswith("`"):
            output.append(f"<code>{html.escape(token[1:-1])}</code>")
        elif token.startswith("["):
            link = re.fullmatch(r"\[([^]]+)\]\(((?:[^()]|\([^()]*\))+)\)", token)
            label, target = link.groups()
            parsed = urlsplit(target.strip())
            if parsed.scheme.lower() in {"", "http", "https", "mailto"}:
                href = html.escape(target.strip(), quote=True)
                output.append(f'<a href="{href}">{html.escape(label)}</a>')
            else:
                output.append(html.escape(label))
        elif token.startswith(("**", "__")):
            output.append(f"<strong>{html.escape(token[2:-2])}</strong>")
        elif token.startswith("~~"):
            output.append(f"<del>{html.escape(token[2:-2])}</del>")
        else:
            output.append(f"<em>{html.escape(token[1:-1])}</em>")

        position = match.end()

    output.append(html.escape(text[position:]))
    return "".join(output)


def body_html(body: str) -> str:
    """Render common block Markdown without trusting embedded HTML."""
    lines = body.splitlines()
    output: list[str] = []
    index = 0

    list_pattern = re.compile(r"^(\s*)([-+*]|\d+[.)])\s+(.*)$")

    def parse_list(position: int, base_indent: int):
        """Parse a list and its indented child lists into a small tree."""
        items = []
        ordered = False

        while position < len(lines):
            match = list_pattern.match(lines[position])
            if not match:
                break

            indent = len(match.group(1).expandtabs(4))
            if indent < base_indent:
                break
            if indent > base_indent:
                if not items:
                    break
                child, position = parse_list(position, indent)
                items[-1]["children"].append(child)
                continue

            marker = match.group(2)
            item_text = match.group(3)
            item_ordered = marker[0].isdigit()
            if not items:
                ordered = item_ordered

            task = re.match(r"^\[([ xX])\]\s+(.*)$", item_text)
            if task:
                checked = task.group(1).lower() == "x"
                checkbox = (
                    '<input type="checkbox" disabled'
                    + (" checked" if checked else "")
                    + "> "
                )
                item_text = checkbox + inline_markdown(task.group(2))
            else:
                item_text = inline_markdown(item_text)

            items.append({"text": item_text, "children": []})
            position += 1

        return {"ordered": ordered, "items": items}, position

    def render_list(node) -> str:
        tag = "ol" if node["ordered"] else "ul"
        parts = [f"<{tag}>"]
        for item in node["items"]:
            parts.append(f"<li>{item['text']}")
            for child in item["children"]:
                parts.append(render_list(child))
            parts.append("</li>")
        parts.append(f"</{tag}>")
        return "".join(parts)

    while index < len(lines):
        line = lines[index]
        stripped = line.strip()

        if not stripped:
            index += 1
            continue

        # Fenced code blocks
        fence = re.match(r"^\s*(```+|~~~+)(.*)$", line)
        if fence:
            marker = fence.group(1)
            language = fence.group(2).strip().split()
            code_lines = []
            index += 1
            while index < len(lines):
                if re.match(r"^\s*" + re.escape(marker[0]) + "{" + str(len(marker)) + r",}\s*$", lines[index]):
                    break
                code_lines.append(lines[index])
                index += 1
            if index < len(lines):
                index += 1
            class_attr = (
                f' class="language-{html.escape(language[0], quote=True)}"'
                if language and re.fullmatch(r"[A-Za-z0-9_-]+", language[0])
                else ""
            )
            code = html.escape("\n".join(code_lines))
            output.append(f"<pre><code{class_attr}>{code}</code></pre>")
            continue

        # Headings
        heading = re.match(r"^\s{0,3}(#{1,6})\s+(.+?)\s*#*\s*$", line)
        if heading:
            level = min(len(heading.group(1)), 6)
            output.append(
                f"<h{level}>{inline_markdown(heading.group(2))}</h{level}>"
            )
            index += 1
            continue

        # Ordered, unordered, and nested lists
        list_match = list_pattern.match(line)
        if list_match:
            indent = len(list_match.group(1).expandtabs(4))
            node, index = parse_list(index, indent)
            output.append(render_list(node))
            continue

        # Blockquotes
        if re.match(r"^\s{0,3}>\s?", line):
            quote_lines = []
            while index < len(lines) and re.match(r"^\s{0,3}>\s?", lines[index]):
                quote_lines.append(re.sub(r"^\s{0,3}>\s?", "", lines[index]))
                index += 1
            output.append(f"<blockquote>{body_html(chr(10).join(quote_lines))}</blockquote>")
            continue

        # Paragraph
        paragraph = [stripped]
        index += 1
        while index < len(lines):
            candidate = lines[index]
            if (
                not candidate.strip()
                or re.match(r"^\s{0,3}(#{1,6}\s|```|~~~|>)", candidate)
                or list_pattern.match(candidate)
            ):
                break
            paragraph.append(candidate.strip())
            index += 1

        output.append(f"<p>{inline_markdown(' '.join(paragraph))}</p>")

    return "\n".join(output)

def source_label(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT.parent.parent))
    except ValueError:
        return str(path)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--database", type=Path, default=ROOT / "control-desk.sqlite3", help="Read active records from a SQLite projection")
    args = parser.parse_args()
    all_records = records(args.database)
    projects = project_roots()
    milestones = [(path, values, body) for path, values, body in all_records if values.get("record_type") == "milestone"]
    complete_statuses = {"complete", "completed", "closed"}
    summary_cards: list[str] = []
    for project_id, (project_name, _) in projects.items():
        project_milestones = [values for _, values, _ in milestones if values.get("project_id") == project_id]
        approved = sum(values.get("status") == "approved" for values in project_milestones)
        proposed = sum(values.get("status") == "proposed" for values in project_milestones)
        high_risk = sum(values.get("risk_level") in {"high", "critical"} for values in project_milestones)
        incomplete = sum(values.get("status") not in complete_statuses for values in project_milestones)
        summary_cards.append(
            f"<article class=\"summary-card\"><h2>{html.escape(project_name)}</h2>"
            f"<p class=\"metric\">{len(project_milestones)} <span>milestones</span></p>"
            f"<p>Approved: {approved} · Proposed: {proposed}</p>"
            f"<p>High/critical risk: {high_risk} · Incomplete: {incomplete}</p></article>"
        )
    cards: list[str] = []
    for path, values, body in milestones:
        milestone_id = values.get("id", "unknown")
        linked = [record for record in all_records if record[1].get("milestone_id") == milestone_id and record[1].get("id") != milestone_id]
        links = ", ".join(html.escape(record[1].get("id", "unknown")) for record in linked) or "none"
        cards.append(
            f"<article class=\"milestone\" data-search=\"{html.escape((milestone_id + ' ' + body).lower(), quote=True)}\" "
            f"data-project=\"{html.escape(values.get('project_id', 'unknown'))}\" "
            f"data-status=\"{html.escape(values.get('status', 'unknown'))}\" "
            f"data-stage=\"{html.escape(values.get('current_stage', 'unknown'))}\" "
            f"data-risk=\"{html.escape(values.get('risk_level', 'unknown'))}\">"
            f"<h2>{html.escape(milestone_id)} — {html.escape(projects.get(values.get('project_id'), (values.get('project_id', 'unknown'), None))[0])}</h2>"
            f"<p><strong>Status:</strong> {html.escape(values.get('status', 'unknown'))} "
            f"<strong>Stage:</strong> {html.escape(values.get('current_stage', 'unknown'))} "
            f"<strong>Risk:</strong> {html.escape(values.get('risk_level', 'unknown'))}</p>"
            f"<p><strong>Linked records:</strong> {links}</p>"
            f"<p><strong>Source:</strong> {html.escape(source_label(path))}</p>"
            f"<details><summary>Record details</summary>{body_html(body)}</details>"
            "</article>"
        )
    document = """<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>STS Control Desk</title><style>
body{font:16px system-ui,sans-serif;max-width:1100px;margin:2rem auto;padding:0 1rem;color:#17202a;background:#f6f8fa}
header,article{background:#fff;border:1px solid #d0d7de;border-radius:10px;padding:1rem 1.25rem;margin:1rem 0}
h1{margin:.2rem 0}.notice{color:#6e3b00;background:#fff8c5;padding:.7rem;border-radius:6px}
.summary-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:.75rem;margin:1rem 0}.summary-card{margin:0}.summary-card h2{font-size:1rem;margin:.1rem 0 .5rem}.metric{font-size:1.8rem;font-weight:700;margin:.2rem 0}.metric span{font-size:1rem;font-weight:400}.summary-note{color:#57606a;font-size:.9rem}
.milestone{box-shadow:0 1px 3px #0001}code{background:#eef1f4;padding:.1rem .25rem;border-radius:3px}
li{margin:.35rem 0}summary{cursor:pointer;font-weight:600}
</style><style>:root{--ink:#17202a;--muted:#667085;--line:#d9e0e8;--canvas:#f4f7fb;--blue:#2563eb;--amber-bg:#fff8df}*{box-sizing:border-box}body{font:15px/1.55 Inter,ui-sans-serif,system-ui,sans-serif;max-width:1240px;padding:28px 22px 64px;background:var(--canvas);color:var(--ink)}header,article{border-radius:16px;box-shadow:0 10px 30px #102a4310}.notice{display:flex;gap:10px;background:var(--amber-bg);border:1px solid #f1d98a;border-radius:10px}.summary-card{padding:16px;background:#fbfcfe}.summary-note{color:var(--muted)}label{font-size:.8rem;font-weight:700;color:var(--muted)}input,select{font:inherit;padding:9px 10px;border:1px solid var(--line);border-radius:8px}button{font:inherit;font-weight:700;background:#e8eef7;border:1px solid #c8d5e6;border-radius:8px;padding:9px 12px;cursor:pointer}button:hover{background:#dce7f5}input:focus,select:focus,button:focus-visible,summary:focus-visible{outline:3px solid #93c5fd;outline-offset:2px}summary{cursor:pointer;font-weight:700;color:var(--blue)}.record-body{border-left:3px solid #d8e4f4;padding-left:16px;margin-top:14px}pre{overflow:auto;background:#f5f7fa;padding:12px;border-radius:8px}@media(max-width:700px){body{padding:16px 12px 40px}.summary-grid{grid-template-columns:repeat(2,minmax(0,1fr))}label{display:block}input,select{width:100%}}@media(prefers-color-scheme:dark){:root{--ink:#e6edf5;--muted:#9aaabd;--line:#304258;--canvas:#0d1624;--amber-bg:#352b12}header,article{background:#111c2c;border-color:var(--line);color:var(--ink)}.summary-card{background:#162235}.notice{color:#f6d77f}input,select{background:#111c2c;color:var(--ink)}code{background:#223047}button{color:#dbeafe;background:#20324a;border-color:#3a516d}}</style></head><body>
<header><h1>STS Control Desk</h1><p class="notice"><strong>READ-ONLY DERIVED VIEW</strong> · Markdown records under <code>control-desk/</code> remain authoritative. Filtering and searching are browser-local and do not modify SQLite or source records.</p>
<p>Projects: __PROJECTS__ · Records: __RECORDS__ · Milestones: __MILESTONES__</p>
<p class="summary-note">Incomplete means the milestone status is not <code>complete</code>, <code>completed</code>, or <code>closed</code>.</p>
<section class="summary-grid">__SUMMARY__</section>
<label>Search <input id="search" type="search" placeholder="ID, project, or record text"></label>
<label>Project <select id="project"><option value="">All</option></select></label>
<label>Status <select id="status"><option value="">All</option></select></label>
<label>Stage <select id="stage"><option value="">All</option></select></label>
<label>Risk <select id="risk"><option value="">All</option></select></label>
<button id="clear" type="button">Reset filters</button>
<p id="result-count"></p></header>
__CARDS__
</body><script>
const cards=[...document.querySelectorAll('.milestone')];
const fields={search:document.querySelector('#search'),project:document.querySelector('#project'),status:document.querySelector('#status'),stage:document.querySelector('#stage'),risk:document.querySelector('#risk')};
const projectNames=__PROJECT_NAMES__;
for(const [value,label] of Object.entries(projectNames)){const option=document.createElement('option');option.value=value;option.textContent=label;fields.project.appendChild(option)}
for(const key of ['status','stage','risk']){const values=[...new Set(cards.map(card=>card.dataset[key]).filter(Boolean))].sort();for(const value of values){const option=document.createElement('option');option.value=value;option.textContent=value;fields[key].appendChild(option)}}
function apply(){const query=fields.search.value.toLowerCase();let visible=0;for(const card of cards){const match=(!query||card.dataset.search.includes(query))&&(!fields.project.value||card.dataset.project===fields.project.value)&&(!fields.status.value||card.dataset.status===fields.status.value)&&(!fields.stage.value||card.dataset.stage===fields.stage.value)&&(!fields.risk.value||card.dataset.risk===fields.risk.value);card.hidden=!match;if(match)visible++}document.querySelector('#result-count').textContent=visible+' of '+cards.length+' milestone(s) shown';}
Object.values(fields).forEach(field=>field.addEventListener('input',apply));document.querySelector('#clear').addEventListener('click',()=>{Object.values(fields).forEach(field=>field.value='');apply()});apply();
</script></html>"""
    project_names = json.dumps({project_id: name for project_id, (name, _) in projects.items()})
    print(document.replace("__PROJECTS__", str(len(projects))).replace("__RECORDS__", str(len(all_records))).replace("__MILESTONES__", str(len(milestones))).replace("__SUMMARY__", "\n".join(summary_cards)).replace("__PROJECT_NAMES__", project_names).replace("__CARDS__", "\n".join(cards)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

