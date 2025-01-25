n = int(input())
arr = list(map(int, input().split()))
min_score = arr[0]
max_score = arr[0]
arr.pop(0)
count = 0
for i in arr:
    if i < min_score:
        count += 1
        min_score = i
    elif i > max_score:
        count += 1
        max_score = i

print(count)