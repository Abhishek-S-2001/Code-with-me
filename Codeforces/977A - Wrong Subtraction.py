n, k = map(int, input().split())

for i in range(k):
    s = str(n)
    if s[-1] == '0':
        n = int(s[:-1])
    else:
        n -= 1
print(n)