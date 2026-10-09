"""Fetch a web page and print its readable text verbatim (stdlib only) — for quoting official sources.

WebFetch summarises; raw `curl` HTML is unreadable. This prints tag-stripped text with whitespace normalised,
so quotes can be copied exactly. Also reports the final URL after redirects and the HTTP status.

Usage:
  python benchtest/tools/fetch_text.py <url>                      # full text
  python benchtest/tools/fetch_text.py <url> --grep "pattern"     # only lines matching a regex (case-insensitive)
  python benchtest/tools/fetch_text.py <url> --context 2 --grep "threshold"
  python benchtest/tools/fetch_text.py <url> --max 400            # first N lines
GitHub source files: use https://github.com/<org>/<repo>/blob/<tag>/<path>?plain=1 or raw URLs.
"""
import argparse
import html
import re
import sys
import urllib.error
import urllib.request
from html.parser import HTMLParser

SKIP = {"script", "style", "noscript", "svg", "head", "template"}
BLOCK = {"p", "div", "li", "tr", "br", "h1", "h2", "h3", "h4", "h5", "h6", "pre", "section", "article",
         "table", "ul", "ol", "dt", "dd", "header", "footer", "blockquote", "td", "th"}


class _Text(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.out, self.skip = [], 0

    def handle_starttag(self, tag, attrs):
        if tag in SKIP:
            self.skip += 1
        elif tag in BLOCK:
            self.out.append("\n")
        if tag in ("td", "th"):
            self.out.append(" | ")

    def handle_endtag(self, tag):
        if tag in SKIP and self.skip:
            self.skip -= 1
        elif tag in BLOCK:
            self.out.append("\n")

    def handle_data(self, data):
        if not self.skip:
            self.out.append(data)


def fetch(url, timeout=30):
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (research; guardrail_research)"})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            body = r.read()
            ctype = r.headers.get("Content-Type", "")
            charset = (re.search(r"charset=([\w-]+)", ctype) or [None, "utf-8"])[1]
            return r.status, r.geturl(), ctype, body.decode(charset, errors="replace")
    except urllib.error.HTTPError as e:
        return e.code, url, e.headers.get("Content-Type", ""), ""


def to_text(raw, ctype):
    if "html" not in ctype and not raw.lstrip().startswith("<"):
        return raw
    p = _Text()
    p.feed(raw)
    text = html.unescape("".join(p.out))
    lines = [re.sub(r"[ \t ]+", " ", ln).strip() for ln in text.splitlines()]
    return "\n".join(ln for ln in lines if ln)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("url")
    ap.add_argument("--grep")
    ap.add_argument("--context", type=int, default=0)
    ap.add_argument("--max", type=int, default=0)
    a = ap.parse_args()
    status, final, ctype, raw = fetch(a.url)
    print(f"# status {status}  final_url {final}  content-type {ctype}")
    if not raw:
        sys.exit(1)
    lines = to_text(raw, ctype).splitlines()
    if a.grep:
        rx = re.compile(a.grep, re.I)
        keep = set()
        for i, ln in enumerate(lines):
            if rx.search(ln):
                keep.update(range(max(0, i - a.context), min(len(lines), i + a.context + 1)))
        lines = [f"{i + 1}: {lines[i]}" for i in sorted(keep)]
    if a.max:
        lines = lines[: a.max]
    sys.stdout.reconfigure(encoding="utf-8")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
