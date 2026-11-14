"""Dependency-free structural checks for the static AURA landing page."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parents[1] / "website"
VOID = set("area base br col embed hr img input link meta param source track wbr".split())

class Page(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.stack, self.ids, self.links, self.errors = [], set(), [], []
        self.title = False

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag not in VOID:
            self.stack.append(tag)
        if tag == "title":
            self.title = True
        if "id" in attrs:
            if attrs["id"] in self.ids:
                self.errors.append(f"Duplicate id: {attrs['id']}")
            self.ids.add(attrs["id"])
        if tag in {"form", "input", "script", "iframe"}:
            self.errors.append(f"Unexpected collection/executable element: {tag}")
        for key in ("href", "src"):
            if key in attrs:
                self.links.append(attrs[key])

    def handle_endtag(self, tag):
        if tag in VOID:
            return
        if not self.stack or self.stack[-1] != tag:
            self.errors.append(f"Mismatched closing tag: {tag}")
        else:
            self.stack.pop()

page = Page()
page.feed((ROOT / "index.html").read_text())
assert page.title, "Missing title"
assert not page.stack, f"Unclosed tags: {page.stack}"
for link in page.links:
    parts = urlsplit(link)
    if parts.scheme:
        assert parts.scheme == "https", f"Unexpected external scheme: {link}"
        assert parts.netloc == "github.com", f"Unexpected external destination: {link}"
    elif parts.path:
        assert (ROOT / parts.path).is_file(), f"Missing asset: {link}"
    elif parts.fragment:
        assert parts.fragment in page.ids, f"Missing anchor: {link}"
assert not page.errors, "\n".join(page.errors)
css = (ROOT / "styles.css").read_text()
assert "prefers-reduced-motion" in css
assert "focus-visible" in css
assert "max-width:720px" in css
print(f"PASS: balanced HTML, {len(page.ids)} IDs, {len(page.links)} links/assets, responsive and keyboard/reduced-motion hooks; no forms or scripts.")
