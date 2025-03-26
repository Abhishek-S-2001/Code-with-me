def find_square_area(t, test_cases):
    for case in test_cases:
        x_vals = set()
        y_vals = set()
        
        for x, y in case:
            x_vals.add(x)
            y_vals.add(y)

        # Get side length
        side_length = abs(max(x_vals) - min(x_vals))  # Or abs(max(y_vals) - min(y_vals))
        
        # Compute area
        print(side_length ** 2)

# Read input
t = int(input().strip())
test_cases = []

for _ in range(t):
    points = [tuple(map(int, input().split())) for _ in range(4)]
    test_cases.append(points)

# Solve for each test case
find_square_area(t, test_cases)
