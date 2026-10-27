# STATUS

## What was built

A beginner manual on coding with AI for free, delivered as Markdown docs plus a static HTML website. Published by Asdale Dynamics, LLC (Indiana, formed October 2026), credited in the README.

**Contents:**
- `README.md` — overview, chapter list, how to use, license
- `LICENSE` — MIT License, copyright line exactly `Copyright (c) 2026 Asdale Dynamics, LLC`
- `docs/` — 8 substantive Markdown chapters:
  1. `00-introduction.md` — welcome, who this is for, how to use
  2. `01-getting-started.md` — install VS Code + Kilo Code extension
  3. `02-free-models.md` — Ollama local models, no-account web chat, free tiers
  4. `03-reading-ai-code.md` — reading AI-written code line by line
  5. `04-fixing-errors.md` — read errors, ask AI for a fix, test again
  6. `05-terminal-safety.md` — safe commands, never `curl | bash`, protect secrets
  7. `06-when-to-ask-human.md` — security, money, production, health, going in circles
  8. `07-first-project.md` — budget note card walkthrough (build, read, run, break, fix, extend)
  9. `08-glossary.md` — plain-English definitions
- `site/` — static HTML website (9 pages + shared `style.css`) mirroring every docs chapter, works by opening `site/index.html` in a browser; nothing to install or serve
- `verify_site.py` — verification script (349 checks, all passing)
- `STATUS.md` — this file

**Audience:** Dylan Asdale, registered nurse turned AI author and founder of Asdale Dynamics, LLC. Plain English, step by step, never condescending. Education only — never medical advice.

## How to run it

- **Read the docs:** open any `docs/*.md` file in a text editor or Markdown viewer.
- **Read the website:** open `site/index.html` in your web browser. No server, no install, no internet needed to read (links are relative).
- **Run the verifier:** `python3 verify_site.py` (Python 3, standard library only). It checks the LICENSE copyright line, README credit, file existence, HTML parsing, internal link resolution, stylesheet links, and scans for secret-like strings.

## Verification results

`python3 verify_site.py` — **All checks passed.** 349 checks, 0 failures.

Verified:
- `LICENSE` exists and contains the exact line `Copyright (c) 2026 Asdale Dynamics, LLC`
- `README.md` exists and credits Asdale Dynamics, LLC
- All 9 docs/ markdown files exist
- All 9 site/ HTML pages exist, parse as HTML, link to `style.css`, have `<title>` tags
- Every internal link in the site resolves to an existing file (including `../LICENSE`)
- `site/style.css` exists
- No secret-like strings (API keys, tokens, private keys) in any tracked file

No build step, no tests framework, no compile errors possible — the site is plain static HTML/Markdown and the verifier is its test suite.

## Known gaps

- No automated spell-check or prose linter; content was reviewed manually
- The HTML site is a mirror of the Markdown docs; if docs are edited, `site/` pages should be updated by hand to match (no build pipeline)
- No search function on the static site (chapter list serves as navigation)
- Ollama/local-model setup and Kilo Code extension availability depend on third-party downloads outside this repo; instructions point to official sources
- Not medical, financial, or legal advice (stated in the glossary and introduction)
