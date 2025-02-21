def is_valid_spelling(s):
    return "YES" if sorted(s) == sorted("Timur") else "NO"

# Read input
t = int(input().strip())

for _ in range(t):
    n = int(input().strip())  # Read n
    s = input().strip()       # Read string s
    print(is_valid_spelling(s))
