n = int(input())
arr = list(map(int, input().split()))

min_idx = n - 1 - list(reversed(arr)).index(min(arr))
max_idx = arr.index(max(arr))
if max_idx > min_idx:
    max_idx -= 1
res = (max_idx) + (n - 1) - min_idx

print(res)