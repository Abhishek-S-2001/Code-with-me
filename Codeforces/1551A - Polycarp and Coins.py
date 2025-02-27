t = int(input())

for _ in range(t):
    n = int(input())

    remainder = n % 3
    c1 = c2 = n // 3
    if remainder == 1:
        c1 += 1
    elif remainder == 2:
        c2 += 1

    print(c1, c2)