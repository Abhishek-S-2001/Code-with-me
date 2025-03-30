def get_ring_score(i, j):
    # Find the minimum distance from the border
    ring = min(i, j, 9 - i, 9 - j)
    return ring + 1  # Convert 0-based to 1-based score

def calculate_score(grid):
    total_score = 0
    for i in range(10):
        for j in range(10):
            if grid[i][j] == 'X':  # If an arrow is present
                total_score += get_ring_score(i, j)
    return total_score

# Read input
t = int(input().strip())
results = []

for _ in range(t):
    grid = [input().strip() for _ in range(10)]  # Read 10x10 grid
    results.append(str(calculate_score(grid)))

# Print all results
print("\n".join(results))
