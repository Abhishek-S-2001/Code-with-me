a = input()
b = input()
s = input()

d1 = {}

for i in a:
    if i not in d1:
        d1[i] = 1
    else:
        d1[i] += 1

for i in b:
    if i not in d1:
        d1[i] = 1
    else:
        d1[i] += 1

d2 = {}
for i in s:
    if i not in d2:
        d2[i] = 1
    else:
        d2[i] += 1

if d1 == d2:
    print('YES')
else:
    print('NO')