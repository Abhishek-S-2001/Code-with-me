t = int(input())

for _ in range(t):
    a, b = map(int, input().split())
    ans = 0
    if a % b != 0:
        x = a // b
        x += 1
        ans = (x * b) - a

    print(ans)