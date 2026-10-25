# Goose + Gmail Agent Lab

A hands-on lab for non-technical learners. Each person installs [Goose](https://goose-docs.ai/), a free, open-source AI agent, on their own laptop. They connect it to a hosted AI model, give it carefully limited access to a Gmail inbox, and teach it an **email-triage skill** written in plain English. No coding and no special hardware are needed.

> **Status: instructor preview.** This version is for instructors to try out and give feedback on before it's adapted for students. The guide ends with an **instructor appendix**: setup, choosing a Gmail path, a dry-run checklist and the lab values card.

## 👉 Open the lab guide

**[Open the lab guide](https://mattquarisa.github.io/goose-lab/)** *(this link works once GitHub Pages is turned on; see "Publishing your own copy" below)*

That's all most people need: it opens in any web browser, and there's nothing to install.

---

## Get your own copy (no technical skills needed)

Want the guide on your own computer, for example to use offline or to look through the files?

1. At the top of this page, click the green **`<> Code`** button.
2. Click **Download ZIP**.
3. Open your **Downloads** folder and unzip the file (double-click it on a Mac; on Windows, right-click → **Extract All**).
4. Open the new `goose-lab` folder and **double-click `index.html`**. The guide opens in your web browser.

<!-- Screenshot suggestion: add a picture of the green Code button menu here, e.g. ![The Code button](docs/code-button.png) -->

**Already use GitHub Desktop?** Choose **`<> Code` → Open with GitHub Desktop** instead. This keeps a linked copy you can update later with one click (**Fetch origin**).

### Just want the skill file?

1. In this repository, open the folders **`skills` → `email-triage`** and click **`SKILL.md`**.
2. Click the **Download raw file** button (the ⬇ icon near the top right of the file).

Or use the **⬇ Download SKILL.md** button inside the lab guide. Either way, the guide explains where to put the file.

---

## What's in the lab

| Part | What learners do |
|---|---|
| 1–2 | Get ready; learn how the AI model, Goose, extensions and skills fit together |
| 3–5 | Install Goose, connect it to a free AI model through OpenRouter, turn on "ask me first" mode |
| 6 | Connect Gmail by one of two paths: **A**, Google's hosted Gmail server (simplest), or **B**, a Gmail program running on the laptop |
| 7–8 | Install, test and customize the email-triage skill |
| 9 | A safety experiment: can an email trick the agent? |
| 10–11 | Clean up; troubleshooting |
| Appendix | Instructor preparation |

Expect about 75–90 minutes, plus about 25 for Gmail Path B.

## What's in this repository

| File or folder | What it is |
|---|---|
| `index.html` | **The lab guide.** One web page; double-click to open. |
| `skills/email-triage/SKILL.md` | **The skill learners install.** Edit the skill here. |
| `README.md` | This page. |
| `scripts/`, `.github/` | Behind-the-scenes helpers. You don't need to touch these. |
| `.gitignore` | Stops password-like files from being uploaded by accident. |

---

## Publishing your own copy

You can do all of this in your web browser, with a free [GitHub account](https://github.com/signup).

### 1. Create the repository

1. On GitHub, click **+** (top right) → **New repository**.
2. Name it `goose-lab`, choose **Public**, and **don't** tick "Add a README file". Click **Create repository**.

### 2. Upload the files

1. On the new, empty repository page, click the **uploading an existing file** link.
2. On your computer, open the unzipped `goose-lab` folder, select **everything inside it**, and drag it onto the GitHub page.
   - Some items start with a dot (`.github`, `.gitignore`, `.nojekyll`) and are **hidden** by default. To show them: on a Mac, press **⌘ + Shift + .** in Finder; on Windows, open File Explorer → **View** → tick **Hidden items**. Make sure you drag these too.
3. Scroll down and click **Commit changes**.

### 3. Turn on the website (GitHub Pages)

1. In your repository, click **Settings** → **Pages** (left menu).
2. Under **Build and deployment**, set **Source** to **Deploy from a branch**, choose branch **main** and folder **/ (root)**, then click **Save**.
3. Wait a minute or two and refresh. GitHub shows your link: `https://mattquarisa.github.io/goose-lab/`.

### 4. Fix the link in this README

Click `README.md`, then the ✏️ pencil icon. Replace `mattquarisa` with your GitHub username, and click **Commit changes**.

> **Private repository?** Free GitHub accounts can only publish the website from public repositories. If you keep the repository private, collaborators can still use **Download ZIP** and double-click `index.html`.

---

## Making changes

You can edit everything on the GitHub website. Click a file, then the ✏️ pencil icon, make your change, and click **Commit changes**. The online guide updates within a minute or two.

- **To change the skill**, edit `skills/email-triage/SKILL.md` only. The guide shows its own copy of the skill, and that copy updates **automatically** a minute after you save. (You may see an extra change from "github-actions[bot]" in the history; that's the automatic update.)
- **To change the guide's text**, edit `index.html`. It's one long web page. Use your browser's find (**Ctrl/⌘ + F**) on GitHub's file view to find the sentence you want, and change only the words between the tags.

<details>
<summary><b>For technical users: git, local preview, manual sync</b></summary>

Clone and preview with a local server, which matches GitHub Pages exactly:

```bash
git clone https://github.com/mattquarisa/goose-lab.git
cd goose-lab
python3 -m http.server 8000     # then open http://localhost:8000
```

When `index.html` is opened directly as a file (`file://`), browsers block it from reading `SKILL.md`, so the page uses its built-in copy. Served over http(s), it loads `skills/email-triage/SKILL.md` and the download button links to that file.

To sync the built-in copy yourself instead of waiting for the GitHub Action:

```bash
python3 scripts/check_skill_sync.py         # check
python3 scripts/check_skill_sync.py --fix   # copy SKILL.md into index.html
```

Fetch only the skill:

```bash
mkdir -p ~/.agents/skills/email-triage
curl -fsSL -o ~/.agents/skills/email-triage/SKILL.md \
  https://raw.githubusercontent.com/mattquarisa/goose-lab/main/skills/email-triage/SKILL.md
```

</details>

---

## ⚠️ Never upload keys or passwords here

The lab uses OpenRouter API keys, Google sign-in files and Gmail accounts. **None of these belong in this repository.** Anything in a public repository can be seen by anyone, and automated bots look for leaked keys within minutes.

- Hand out the filled-in **lab values card** privately (on paper, or by direct message), never by uploading it.
- Never upload files named like `client_secret_….json`, `gcp-oauth.keys.json` or `credentials.json`.
- If a key is ever uploaded by mistake, **cancel it and make a new one** in the service that issued it. Deleting the file from GitHub isn't enough.

## Running the lab as an instructor

Before your session, read the **instructor appendix** at the end of the guide. It covers:

- setting up **OpenRouter** (Appendix F): creating the account, choosing a free (`:free`) model that supports tools, and making a spending-capped API key for each learner. Note that free models share a small rate limit across the whole class;
- choosing **Gmail Path A** (you set up one Google Cloud project for the class) or **Path B** (each learner sets up their own);
- a **dry-run checklist**. Please try it on at least one Mac and one Windows laptop, because Goose's menus change between versions.

## Feedback

Tried the lab? Please share what worked and what didn't. In this repository, click **Issues** → **New issue** → **Lab feedback**. Before attaching screenshots, remove any keys, passwords or email content.

## Credits and references

- [goose documentation](https://goose-docs.ai/)
- [Configure the Gmail MCP server](https://developers.google.com/workspace/gmail/api/guides/configure-mcp-server) (Google)
- [`@gongrzhe/server-gmail-autoauth-mcp`](https://www.npmjs.com/package/@gongrzhe/server-gmail-autoauth-mcp) (community Gmail server used in Path B)
- [Agent Skills](https://agentskills.io/) (the open `SKILL.md` format)

Goose and Gmail are trademarks of their respective owners. This lab isn't affiliated with or endorsed by Block, the Agentic AI Foundation or Google.

## License

*No license has been chosen yet.* Until one is added, others can view this lab but don't have permission to reuse or adapt it. To let other instructors adapt it, add a license: click **Add file → Create new file**, name it `LICENSE`, then click **Choose a license template**. For example, **CC BY 4.0** is a common choice for teaching materials. If it isn't in GitHub's list, paste its text from [creativecommons.org](https://creativecommons.org/licenses/by/4.0/legalcode.txt) instead.
