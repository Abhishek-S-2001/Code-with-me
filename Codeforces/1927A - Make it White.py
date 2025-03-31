def min_paint_length(n, s):
    left = s.find('B')     # First occurrence of 'B'
    right = s.rfind('B')   # Last occurrence of 'B'
    return right - left + 1

# Read input
t = int(input().strip())  # Number of test cases
results = []

for _ in range(t):
    n = int(input().strip())  # Length of the strip
    s = input().strip()       # Strip of cells
    results.append(str(min_paint_length(n, s)))

# Print all results at once for efficiency
print("\n".join(results))
