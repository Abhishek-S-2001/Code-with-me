t = int(input())
for _ in range(t):
    arr = list(map(int, input().split()))

    a = arr[0]
    count = 0
    for i in arr:
        if i > a:
            count += 1
    print(count)