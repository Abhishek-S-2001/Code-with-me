import math

def is_perfect_square(x):
    sqrt_x = int(math.sqrt(x))
    return sqrt_x * sqrt_x == x

# Read number of test cases
t = int(input())
results = []

for _ in range(t):
    n = int(input())  # Number of buckets
    a = list(map(int, input().split()))  # List of squares in each bucket
    total_squares = sum(a)  # Compute total sum

    # Check if it's a perfect square
    print("YES" if is_perfect_square(total_squares) else "NO")
