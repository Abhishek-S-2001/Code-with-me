n = int(input())
arr = list(map(int, input().split()))
count = 0
res = 0
for i in arr: 
    count += i
    if count < 0:
        res += abs(count)
        count = 0

print(res)