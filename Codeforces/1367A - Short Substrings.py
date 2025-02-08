def reconstruct_string(test_cases):
    results = []
    for b in test_cases:
        a = b[0]  # Start with the first character
        for i in range(1, len(b), 2):  # Take every second character
            a += b[i]
        results.append(a)
    return results

# Read input
t = int(input())
test_cases = [input().strip() for _ in range(t)]

# Process and print results
for result in reconstruct_string(test_cases):
    print(result)
