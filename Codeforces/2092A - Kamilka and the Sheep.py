import sys
import math

def max_possible_gcd(n, beauty_levels):
    min_beauty = min(beauty_levels)  # Find the smallest beauty level
    diff_gcd = 0  # Start with 0 since GCD(x, 0) = x
    
    for beauty in beauty_levels:
        diff_gcd = math.gcd(diff_gcd, beauty - min_beauty)
    
    return diff_gcd

# Reading input
t = int(sys.stdin.readline().strip())  # Number of test cases
results = []

for _ in range(t):
    n = int(sys.stdin.readline().strip())  # Number of sheep
    beauty_levels = list(map(int, sys.stdin.readline().split()))  # Beauty levels of the sheep
    
    results.append(str(max_possible_gcd(n, beauty_levels)))

# Print all results efficiently
sys.stdout.write("\n".join(results) + "\n")
