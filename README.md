# Goose Agent Lab

A hands-on lab for non-technical learners. Each person installs [Goose](https://goose-docs.ai/), a free, open-source AI agent, on their own laptop, connects it to a hosted AI model, and gives it new abilities in plain English: first a **RESA assistant** skill that answers from private files on the laptop, then a connection to **Notion** through its hosted MCP server so the agent can read and update real pages. No coding and no special hardware are needed.

> **Status: instructor preview.** This version is for instructors to try out and give feedback on before it's adapted for students. The guide ends with an **instructor appendix**: setup, a dry-run checklist and the lab values card.

## 👉 Open the lab guide

**[Open the lab guide](https://mattquarisa.github.io/goose-lab/)** *(this link works once GitHub Pages is turned on; see "Publishing your own copy" below)*

That's all most people need: it opens in any web browser, and there's nothing to install.

## What's in the lab

| Part | What learners do |
|---|---|
| 1–2 | Get ready; learn how the AI model, Goose, extensions and skills fit together |
| 3–5 | Install Goose, connect it to a free AI model through OpenRouter, turn on "ask me first" mode |
| 6 | First agent task: Goose builds a small app (live date and time, plus a thank-you message) and hosts it in its **Apps** section |
| 7 | **First skill:** a private RESA assistant that answers from local files (events, FAQs) using the Developer extension — this is where skills are introduced |
| 8 | **Connect a real tool:** add Notion through its hosted MCP server (one-click browser sign-in) and have the agent read and update pages |
| 9 | A safety experiment: can a shared Notion page trick the agent? |
| 10–11 | Clean up; troubleshooting |
| Appendix | Instructor preparation, including OpenRouter setup |

Expect about 75–90 minutes.

## What's in this repository

| File or folder | What it is |
|---|---|
| `index.html` | **The lab guide.** One web page; double-click to open. |
| `skills/resa-assistant/SKILL.md` | **The RESA assistant skill** (the first skill, Part 7). Edit it here. |
| `resa-docs-test/` | **Sample documents** (a made-up student club, RESA) the RESA assistant reads in Part 7, with the source PDFs and their converted Markdown. |
| `course-info/` | **Sample course documents** (made-up courses) for the Part 7 course practice, in the same shape: source PDFs plus their converted Markdown. |
| `README.md` | This page. |
| `scripts/`, `.github/` | Behind-the-scenes helpers. You don't need to touch these. |
| `.gitignore` | Stops password-like files from being uploaded by accident. |