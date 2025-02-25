t = int(input())

for _ in range(t):
    n = int(input())
    s = list(input())
    seen = set()
    count = 0
    for i in s:
        if i not in seen:
            count += 2
            seen.add(i)
        else:
            count += 1

    print(count)