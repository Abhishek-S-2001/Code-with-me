# Read number of test cases
t = int(input().strip())

for _ in range(t):
    n = int(input().strip())  # Read n
    arr = list(map(int, input().strip().split()))  # Read array
    print(max(arr) - min(arr))
