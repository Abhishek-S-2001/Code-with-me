import sys

# Read number of test cases
t = int(sys.stdin.readline().strip())

for _ in range(t):
    # Read n
    n = int(sys.stdin.readline().strip())

    # Read the 2n numbers
    arr = list(map(int, sys.stdin.readline().split()))

    # Count odd and even numbers
    odd_count = sum(1 for num in arr if num % 2 == 1)
    even_count = 2 * n - odd_count  # Remaining numbers are even

    # If we have equal numbers of odd and even, it's possible
    print("Yes" if odd_count == even_count else "No")
