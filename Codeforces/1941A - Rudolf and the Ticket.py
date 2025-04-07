t = int(input())
for _ in range(t):
    n, m, k = map(int, input().split())
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))
    
    count = 0
    for bi in b:
        for cj in c:
            if bi + cj <= k:
                count += 1
    print(count)
