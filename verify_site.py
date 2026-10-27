#!/usr/bin/env python3
"""Verification script for the Free AI Coding for Beginners guide.

Checks:
  * LICENSE contains the exact MIT copyright line
  * README credits Asdale Dynamics, LLC
  * All docs/ markdown files exist
  * All site/ HTML files exist, parse as HTML, and reference style.css
  * Internal links resolve to existing files
  * No secrets/API-key-looking strings in any file

Run:  python3 verify_site.py
Exit code: 0 if all checks pass, non-zero otherwise.
"""
from __future__ import annotations

import html
import os
import re
import sys
from html.parser import HTMLParser
from urllib.parse import urljoin, urlparse

ROOT = os.path.dirname(os.path.abspath(__file__))
SITE = os.path.join(ROOT, "site")
DOCS = os.path.join(ROOT, "docs")

EXPECTED_COPYRIGHT = "Copyright (c) 2026 Asdale Dynamics, LLC"

failures = []
checks = 0


def check(condition, message):
    global checks
    checks += 1
    if condition:
        print(f"PASS: {message}")
    else:
        failures.append(message)
        print(f"FAIL: {message}")


# ---------- LICENSE ----------
license_path = os.path.join(ROOT, "LICENSE")
check(os.path.isfile(license_path), "LICENSE file exists at repo root")

license_text = ""
if os.path.isfile(license_path):
    with open(license_path, encoding="utf-8") as f:
        license_text = f.read()
check(EXPECTED_COPYRIGHT in license_text,
      f"LICENSE contains exact copyright line: {EXPECTED_COPYRIGHT!r}")
check("MIT License" in license_text, "LICENSE is the MIT License")

# ---------- README ----------
readme_path = os.path.join(ROOT, "README.md")
check(os.path.isfile(readme_path), "README.md exists at repo root")
readme_text = ""
if os.path.isfile(readme_path):
    with open(readme_path, encoding="utf-8") as f:
        readme_text = f.read()
check("Asdale Dynamics, LLC" in readme_text,
      "README credits Asdale Dynamics, LLC")
check(EXPECTED_COPYRIGHT in readme_text,
      f"README contains copyright line: {EXPECTED_COPYRIGHT!r}")

# ---------- docs ----------
expected_docs = [
    "00-introduction.md",
    "01-getting-started.md",
    "02-free-models.md",
    "03-reading-ai-code.md",
    "04-fixing-errors.md",
    "05-terminal-safety.md",
    "06-when-to-ask-human.md",
    "07-first-project.md",
    "08-glossary.md",
]
for name in expected_docs:
    check(os.path.isfile(os.path.join(DOCS, name)), f"docs/{name} exists")

# ---------- site pages ----------
expected_pages = [
    "index.html",
    "getting-started.html",
    "free-models.html",
    "reading-ai-code.html",
    "fixing-errors.html",
    "terminal-safety.html",
    "when-to-ask-human.html",
    "first-project.html",
    "glossary.html",
]


class LinkCollector(HTMLParser):
    """Collect href/src attributes and raw text from an HTML document."""

    def __init__(self):
        super().__init__()
        self.links = []
        self.text_parts = []

    def handle_starttag(self, tag, attrs):
        for attr, value in attrs:
            if attr in ("href", "src") and value:
                self.links.append(value)

    def handle_data(self, data):
        self.text_parts.append(data)

    def get_text(self):
        return html.unescape("".join(self.text_parts))


for name in expected_pages:
    path = os.path.join(SITE, name)
    check(os.path.isfile(path), f"site/{name} exists")

    with open(path, encoding="utf-8") as f:
        content = f.read()

    # basic well-formedness: parse without raising
    try:
        parser = LinkCollector()
        parser.feed(content)
        text = parser.get_text()
    except Exception as exc:  # pragma: no cover - HTMLParser rarely raises
        check(False, f"site/{name} parses as HTML ({exc})")
        continue
    check(True, f"site/{name} parses as HTML")

    # references the shared stylesheet
    check("style.css" in content, f"site/{name} links to style.css")

    # title present
    check(bool(re.search(r"<title[^>]*>.*?</title>", content, re.S | re.I)),
          f"site/{name} has a <title>")

    # internal links resolve
    for link in parser.links:
        if link.startswith(("http://", "https://", "mailto:", "tel:")):
            continue  # external, not checked here
        parsed = urlparse(link)
        target = os.path.normpath(os.path.join(os.path.dirname(path), parsed.path or "index.html"))
        check(os.path.isfile(target),
              f"site/{name}: link {link!r} resolves to existing file ({target})")

# ---------- CSS ----------
css_path = os.path.join(SITE, "style.css")
check(os.path.isfile(css_path), "site/style.css exists")

# ---------- secrets scan ----------
secret_patterns = [
    re.compile(r"sk-[A-Za-z0-9]{20,}"),          # OpenAI-style keys
    re.compile(r"AIza[0-9A-Za-z\-_]{35,}"),      # generic API key
    re.compile(r"ghp_[A-Za-z0-9]{20,}"),         # GitHub tokens
    re.compile(r"xox[baprs]-[0-9A-Za-z\-]{10,}"), # Slack tokens
    re.compile(r"-----BEGIN [A-Z ]+PRIVATE KEY-----"),  # private keys
]
text_files = []
for dirpath, _dirs, files in os.walk(ROOT):
    # skip .git
    if ".git" in dirpath.split(os.sep):
        continue
    for fn in files:
        if fn.endswith((".md", ".html", ".css", ".py", ".txt", ".json", ".license")):
            text_files.append(os.path.join(dirpath, fn))

for path in text_files:
    try:
        with open(path, encoding="utf-8", errors="ignore") as f:
            data = f.read()
    except OSError:
        continue
    for pat in secret_patterns:
        check(not pat.search(data),
              f"No secret-like string in {os.path.relpath(path, ROOT)}")

# ---------- summary ----------
print()
print(f"Checks run: {checks}")
print(f"Failures:   {len(failures)}")
if failures:
    print("\nFailures:")
    for f in failures:
        print("  -", f)
    sys.exit(1)
print("All checks passed.")
sys.exit(0)
