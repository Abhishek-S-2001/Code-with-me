import sys

def min_lanterns(n, m):
    return (n * m + 1) // 2  # Ceiling division using integer arithmetic

# Read number of test cases
t = int(sys.stdin.readline().strip())
results = []

# Process each test case
for _ in range(t):
    n, m = map(int, sys.stdin.readline().split())
    results.append(str(min_lanterns(n, m)))

# Print all results efficiently
sys.stdout.write("\n".join(results) + "\n")
