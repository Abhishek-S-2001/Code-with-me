def can_reduce_to_one(arr):
    arr.sort()  # Sort the array
    for i in range(len(arr) - 1):
        if abs(arr[i] - arr[i + 1]) > 1:
            return "NO"
    return "YES"

# Read number of test cases
t = int(input())
for _ in range(t):
    n = int(input())  # Number of elements in the array
    arr = list(map(int, input().split()))  # The array
    print(can_reduce_to_one(arr))