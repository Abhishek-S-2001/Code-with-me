arr = list(map(int, input().split()))
res = []
m = max(arr)
for i in arr:
    if m == i:
        continue
    res.append(m - i)

for i in res:
    print(i, end=" ")