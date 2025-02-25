t = int(input())

for _ in range(t):
    h, m = map(int, input().split())

    h = 23 - h
    m = 60 - m
    rm = h * 60 + m

    print(rm)