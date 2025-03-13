def can_find_subsegment(n, k, a):
    count_k = a.count(k)
    
    if count_k >= 2:
        return "YES"
    if n == 1 and a[0] == k:
        return "YES"
    
    return "NO"

# Read input
t = int(input())
results = []

for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    results.append(can_find_subsegment(n, k, a))

# Output results
print("\n".join(results))
