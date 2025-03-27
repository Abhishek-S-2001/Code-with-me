def min_moves_to_equal_gifts(t, test_cases):
    results = []
    
    for case in test_cases:
        n, candies, oranges = case
        min_candies = min(candies)
        min_oranges = min(oranges)
        
        total_moves = 0
        for i in range(n):
            total_moves += max(candies[i] - min_candies, oranges[i] - min_oranges)
        
        results.append(total_moves)
    
    return results

# Reading input
t = int(input().strip())
test_cases = []

for _ in range(t):
    n = int(input().strip())
    candies = list(map(int, input().split()))
    oranges = list(map(int, input().split()))
    test_cases.append((n, candies, oranges))

# Computing results
results = min_moves_to_equal_gifts(t, test_cases)

# Output results
for res in results:
    print(res)
