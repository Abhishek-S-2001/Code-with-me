n, h = map(int, input().split())
arr = list(map(int, input().split()))
res = 0
for i in arr:
    if i <= h:
        res += 1
    else:
        res += 2
print(res)