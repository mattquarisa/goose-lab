# Goose + Gmail Agent Lab

A hands-on lab for non-technical learners. Each person installs [Goose](https://goose-docs.ai/), a free, open-source AI agent, on their own laptop, connects it to a hosted AI model, and teaches it **skills** written in plain English: first a **course assistant** that answers from private files on the laptop, then an **email-triage skill** for a Gmail inbox it's given carefully limited access to. No coding and no special hardware are needed.

> **Status: instructor preview.** This version is for instructors to try out and give feedback on before it's adapted for students. The guide ends with an **instructor appendix**: setup, choosing a Gmail path, a dry-run checklist and the lab values card.

## 👉 Open the lab guide

**[Open the lab guide](https://mattquarisa.github.io/goose-lab/)** *(this link works once GitHub Pages is turned on; see "Publishing your own copy" below)*

That's all most people need: it opens in any web browser, and there's nothing to install.

## What's in the lab

| Part | What learners do |
|---|---|
| 1–2 | Get ready; learn how the AI model, Goose, extensions and skills fit together |
| 3–5 | Install Goose, connect it to a free AI model through OpenRouter, turn on "ask me first" mode |
| 6 | First agent task: Goose builds a small app (live date and time, plus a thank-you message) and hosts it in its **Apps** section |
| 7 | **First skill:** a private course assistant that answers from local files (room, time, instructor) using the Developer extension — this is where skills are introduced |
| 8 | Connect Gmail by one of two paths: **A**, Google's hosted Gmail server (simplest), or **B**, a Gmail program running on the laptop |
| 9–10 | Install, test and customize a second skill, email-triage |
| 11 | A safety experiment: can an email trick the agent? |
| 12–13 | Clean up; troubleshooting |
| Appendix | Instructor preparation, including OpenRouter setup |

Expect about 105–120 minutes, plus about 25 for Gmail Path B.

## What's in this repository

| File or folder | What it is |
|---|---|
| `index.html` | **The lab guide.** One web page; double-click to open. |
| `skills/course-assistant/SKILL.md` | **The course-assistant skill** (the first skill, Part 7). Edit it here. |
| `skills/email-triage/SKILL.md` | **The email-triage skill** (the second skill, Part 9). Edit it here. |
| `course-info/` | **Sample private documents** (made-up courses) the course assistant reads in Part 7. |
| `README.md` | This page. |
| `scripts/`, `.github/` | Behind-the-scenes helpers. You don't need to touch these. |
| `.gitignore` | Stops password-like files from being uploaded by accident. |