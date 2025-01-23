from pathlib import Path
from re import X
import shutil

copy_globs = ['*.css', '*.js', '*.png']
page_globs = ['**/*.txt']
template = Path('template.html')
src = Path('src/')
dist = Path('dist/')

if dist.exists():
    shutil.rmtree(dist)

to_copy = []

for x in copy_globs:
    to_copy.extend(src.glob(x))

pages = []

for x in page_globs:
    pages.extend(src.glob(x))

dist.mkdir(exist_ok=True)

for x in to_copy:
    dest = dist / x.relative_to(src)
    dest.parent.mkdir(exist_ok=True)
    shutil.copy(x, dest)

t = ''
with open(src / template, 'r') as f:
    t = f.read()

for x in pages:
    page = ''
    dest = dist / x.relative_to(src).with_suffix('.html')
    dest.parent.mkdir(exist_ok=True)
    with open(x, 'r') as f:
        page = t.format(content=f.read())
    with open(dest, '+w') as f:
        f.write(page)
