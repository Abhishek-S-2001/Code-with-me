a, b = map(int, input().split())
res = []
x = 0
if a > b:
    res.append(b)
    x = a - b
    res.append(x // 2)
else:
    res.append(a)
    x = b - a
    res.append(x // 2)

for i in res:
    print(i, end=" ")