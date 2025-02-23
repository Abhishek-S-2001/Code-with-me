def determine_winner(n):
    if n % 3 == 0:
        return "Second"
    return "First"

# Read number of test cases
t = int(input().strip())

for _ in range(t):
    n = int(input().strip())
    print(determine_winner(n))
