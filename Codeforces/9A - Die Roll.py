import math

def find_probability(Y, W):
    max_roll = max(Y, W)  # Dot needs at least this value
    favorable = 6 - max_roll + 1  # Count of favorable outcomes
    gcd = math.gcd(favorable, 6)  # Simplify the fraction
    print(f"{favorable // gcd}/{6 // gcd}")

# Input Handling
Y, W = map(int, input().split())
find_probability(Y, W)
