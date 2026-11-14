"""Stage the selected landing page at the GitHub Pages root, retaining old URLs."""
from pathlib import Path
import shutil

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / '_site'
if OUTPUT.exists():
    shutil.rmtree(OUTPUT)
OUTPUT.mkdir()
# Preserve previous public URLs and the original design.
shutil.copytree(ROOT / 'website', OUTPUT / 'website')
# Publish the chosen design at /Aura/.
shutil.copytree(ROOT / 'website' / 'nordic-orbit', OUTPUT, dirs_exist_ok=True)
shutil.copy2(ROOT / 'website' / 'icon.svg', OUTPUT / 'icon.svg')
page = OUTPUT / 'index.html'
page.write_text(page.read_text().replace('href="../icon.svg"', 'href="icon.svg"')
                .replace('href="../"', 'href="website/"'))
(OUTPUT / '.nojekyll').touch()
print('Pages ready in _site/: selected design at root; previous URLs retained.')
