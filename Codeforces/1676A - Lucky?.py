t = int(input())
for _ in range(t):
    arr = list(map(int, input().strip()))

    if sum(arr[:3]) == sum(arr[3:]):
        print("YES")
    else:
        print("NO")