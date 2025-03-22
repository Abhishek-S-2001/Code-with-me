t = int(input())

for _ in range(t):
    n = int(input())
    res = 0
    if n >= 4:
        res += n // 4
        n = n % 4
    
    if n >= 2:
        res += 1
    
    print(res)