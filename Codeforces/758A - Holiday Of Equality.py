n = int(input())
arr = list(map(int,input().split()))
m = max(arr)
ans = 0
for i in arr:
    if i < m:
        ans += m - i
print(ans)