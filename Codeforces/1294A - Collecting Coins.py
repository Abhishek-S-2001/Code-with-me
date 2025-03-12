def can_distribute_coins(a, b, c, n):
    max_coins = max(a, b, c)
    required = (max_coins - a) + (max_coins - b) + (max_coins - c)
    
    if n >= required and (n - required) % 3 == 0:
        return "YES"
    else:
        return "NO"

# Reading input
t = int(input())  # Number of test cases
results = []

for _ in range(t):
    a, b, c, n = map(int, input().split())
    results.append(can_distribute_coins(a, b, c, n))

# Output results
print("\n".join(results))
