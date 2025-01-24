from pathlib import Path
import shutil

copy_globs = ['*.css', '*.js', '*.png', '*.svg', '*.jpg', '*.gif', 'CNAME']
page_globs = ['**/*.html', '**/*.txt']
src = Path('src/')
dist = Path('dist/')
home = src / 'home.html'
template = src / 'template.html'

if dist.exists():
    shutil.rmtree(dist)

to_copy = []

for x in copy_globs:
    to_copy.extend(src.glob(x))

pages = []

for x in page_globs:
    pages.extend(src.glob(x))

pages = [x for x in pages if x not in to_copy and x != template ]

dist.mkdir(exist_ok=True)

for x in to_copy:
    dest = dist / x.relative_to(src)
    dest.parent.mkdir(exist_ok=True)
    shutil.copy(x, dest)

t = ''
with open(template, 'r') as f:
    t = f.read()

for x in pages:
    page = ''

    dest = dist / x.relative_to(src).with_suffix('') / 'index.html'
    if x == home:
        dest = dist / 'index.html'
    dest.parent.mkdir(exist_ok=True)
    with open(x, 'r') as f:
        page = t.format(content=f.read())
    with open(dest, '+w') as f:
        f.write(page)
