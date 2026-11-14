"""Structural and asset-link checks for the separate Nordic Orbit concept."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parents[1] / 'website' / 'nordic-orbit'
VOID = set('area base br col embed hr img input link meta param source track wbr'.split())

class Check(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids, self.links, self.stack = set(), [], []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag not in VOID:
            self.stack.append(tag)
        if 'id' in attrs:
            assert attrs['id'] not in self.ids, 'Duplicate ID'
            self.ids.add(attrs['id'])
        assert tag not in {'form', 'input', 'iframe'}, tag
        if tag == 'script':
            assert attrs.get('src') == 'theme.js', 'Unexpected script'
        for key in ('href', 'src'):
            if key in attrs:
                self.links.append(attrs[key])

    def handle_startendtag(self, tag, attrs):
        self.handle_starttag(tag, attrs)
        if tag not in VOID:
            self.handle_endtag(tag)

    def handle_endtag(self, tag):
        assert self.stack and self.stack.pop() == tag, f'Mismatched tag: {tag}'

page = Check()
page.feed((ROOT / 'index.html').read_text())
assert not page.stack, f'Unclosed tags: {page.stack}'
for url in page.links:
    parts = urlsplit(url)
    if parts.scheme:
        assert parts.scheme == 'https' and parts.netloc == 'github.com', url
    elif parts.path:
        assert (ROOT / parts.path).exists(), f'Missing asset: {url}'
    elif parts.fragment:
        assert parts.fragment in page.ids, f'Missing anchor: {url}'
print('PASS: Nordic Orbit HTML structure and all local links/assets/anchors.')
