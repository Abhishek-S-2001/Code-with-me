s = set(input())
if '{' in s:
    s.remove('{')
if '}' in s:
    s.remove('}')
if ' ' in s:
    s.remove(' ')
if ',' in s:
    s.remove(',')

print(len(s))