a, b, c, d = map(int, input().split())
s = list(input())
res = 0
for i in s:
    if i == '1':
        res += a
    elif i == '2':
        res += b
    elif i == '3':
        res += c
    elif i == '4':
        res += d
print(res)