t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    freq = {}
    for i in range(n):
        if arr[i] not in freq:
            freq[arr[i]] = [i + 1]
        else:
            freq[arr[i]].append(i + 1)

    for k, v in freq.items():
        if len(v) == 1:
            print(v[0])