def is_square_string(s):
    n = len(s)
    if n % 2 == 1:
        return "NO"
    return "YES" if s[:n//2] == s[n//2:] else "NO"

# Read number of test cases
t = int(input())

# Process each test case
for _ in range(t):
    s = input()
    print(is_square_string(s))