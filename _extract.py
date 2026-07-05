import re

text = open(r'E:/tetea/XBizzard/tetea-chaos.html', 'r', encoding='utf-8').read()

m = re.search(r'const SCATTER=(\[.*?\]);', text, re.DOTALL)
s = eval(m.group(1)) if m else []

m2 = re.search(r'const GRID=(\[.*?\]);', text, re.DOTALL)
g = eval(m2.group(1)) if m2 else []

m3 = re.search(r'const VIDS=(\[.*?\]);', text, re.DOTALL)
v = eval(m3.group(1)) if m3 else []

print(f'// SCATTER: {len(s)} items')
for x in s:
    print(repr(x) + ',')

print(f'\n// GRID: {len(g)} items')
for x in g:
    print(repr(x) + ',')

print(f'\n// VIDS: {len(v)} items')
for x in v:
    print(repr(x) + ',')
