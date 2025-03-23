t = int(input())

for _ in range(t):
    n = int(input())
    s = list(map(int, input().split()))

    s.sort()
    min_diff = min(s[i+1] - s[i] for i in range(n-1))
        
    print(str(min_diff))