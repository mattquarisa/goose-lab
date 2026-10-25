#!/usr/bin/env python3
"""Check that the skill shown inside index.html matches skills/email-triage/SKILL.md.

index.html keeps an inline copy of the skill so the guide still works when it is
opened straight from disk (file://), where browsers block reading other files.
Run this after editing either copy:

    python3 scripts/check_skill_sync.py          # check only
    python3 scripts/check_skill_sync.py --fix    # copy SKILL.md into index.html

SKILL.md is the source of truth; --fix never changes it.
"""
import html
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
PAGE = ROOT / "index.html"
SKILL = ROOT / "skills" / "email-triage" / "SKILL.md"
PATTERN = re.compile(r'(<code id="skill-text">)(.*?)(</code>)', re.S)


def main() -> int:
    page = PAGE.read_text(encoding="utf-8")
    skill = SKILL.read_text(encoding="utf-8").rstrip("\n")
    match = PATTERN.search(page)
    if not match:
        print("Could not find <code id=\"skill-text\"> in index.html")
        return 2

    inline = html.unescape(match.group(2))
    if inline == skill:
        print("OK: index.html matches skills/email-triage/SKILL.md")
        return 0

    if "--fix" in sys.argv:
        escaped = html.escape(skill, quote=False)
        page = page[: match.start(2)] + escaped + page[match.end(2):]
        PAGE.write_text(page, encoding="utf-8")
        print("Fixed: copied SKILL.md into index.html")
        return 0

    print("MISMATCH: the skill in index.html differs from skills/email-triage/SKILL.md.")
    print("Edit SKILL.md, then run: python3 scripts/check_skill_sync.py --fix")
    return 1


if __name__ == "__main__":
    sys.exit(main())
