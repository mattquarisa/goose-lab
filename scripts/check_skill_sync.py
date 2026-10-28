#!/usr/bin/env python3
"""Check that the skills shown inside index.html match their SKILL.md files.

index.html keeps an inline copy of each skill so the guide still works when it is
opened straight from disk (file://), where browsers block reading other files.
Each embed is a <code id="..."> block tied to one SKILL.md below. Run this after
editing either copy:

    python3 scripts/check_skill_sync.py          # check only
    python3 scripts/check_skill_sync.py --fix    # copy each SKILL.md into index.html

The SKILL.md files are the source of truth; --fix never changes them.
"""
import html
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
PAGE = ROOT / "index.html"

# Each entry maps a <code id="..."> block in index.html to its source SKILL.md.
SKILLS = {
    "skill-text": ROOT / "skills" / "email-triage" / "SKILL.md",
    "skill-text-course": ROOT / "skills" / "course-assistant" / "SKILL.md",
}


def main() -> int:
    page = PAGE.read_text(encoding="utf-8")
    fix = "--fix" in sys.argv
    changed = False
    mismatches = []

    for code_id, skill_path in SKILLS.items():
        skill = skill_path.read_text(encoding="utf-8").rstrip("\n")
        pattern = re.compile(
            r'(<code id="' + re.escape(code_id) + r'">)(.*?)(</code>)', re.S
        )
        match = pattern.search(page)
        if not match:
            print(f'Could not find <code id="{code_id}"> in index.html')
            return 2

        if html.unescape(match.group(2)) == skill:
            continue

        if fix:
            escaped = html.escape(skill, quote=False)
            page = page[: match.start(2)] + escaped + page[match.end(2):]
            changed = True
        else:
            mismatches.append(skill_path.relative_to(ROOT))

    if fix:
        if changed:
            PAGE.write_text(page, encoding="utf-8")
            print("Fixed: copied skills into index.html")
        else:
            print("OK: index.html already matches every SKILL.md")
        return 0

    if mismatches:
        joined = ", ".join(str(p) for p in mismatches)
        print(f"MISMATCH: index.html differs from: {joined}.")
        print("Edit the SKILL.md, then run: python3 scripts/check_skill_sync.py --fix")
        return 1

    print("OK: index.html matches every SKILL.md")
    return 0


if __name__ == "__main__":
    sys.exit(main())
