def max_teams(n, k, participation_counts):
    eligible_students = sum(1 for y in participation_counts if y + k <= 5)
    return eligible_students // 3

# Read input
n, k = map(int, input().split())
participation_counts = list(map(int, input().split()))

# Compute and print the result
print(max_teams(n, k, participation_counts))
