import sys

def can_mihai_win(n, candies):
    evens = [x for x in candies if x % 2 == 0]
    odds = [x for x in candies if x % 2 != 0]

    # Compute total sums
    sum_even = sum(evens)
    sum_odd = sum(odds)

    # Mihai must have a strictly greater sum
    return "YES" if sum_even > sum_odd else "NO"

# Read input
t = int(sys.stdin.readline().strip())  # Number of test cases
results = []

for _ in range(t):
    n = int(sys.stdin.readline().strip())  # Number of bags
    candies = list(map(int, sys.stdin.readline().split()))  # Candy values
    
    results.append(can_mihai_win(n, candies))

# Print all results at once
sys.stdout.write("\n".join(results) + "\n")
