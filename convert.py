#!/usr/bin/env python3

import re
import urllib.parse
from pathlib import Path

pth = Path('.')
pat1 = re.compile(r'!\[\[([^\]]+)\]\]')
pat2 = re.compile(r'\[\[([^\]]+)\]\]')

def sub1(x):
    url = urllib.parse.quote(x[1])
    return f'![]({url})'
def sub2(x):
    url = urllib.parse.quote(x[1])
    return f'[{x[1]}]({url})'

for p in pth.glob('*.md'):
    with open(p) as f:
        d = f.read()
    d = pat1.sub(sub1, d)
    d = pat2.sub(sub2, d)
    with open(p, 'w') as f:
        f.write(d)
