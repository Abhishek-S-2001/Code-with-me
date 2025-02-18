def min_swaps_to_good_array(n, arr):
    wrong_even = 0  # Even indices having odd values
    wrong_odd = 0   # Odd indices having even values

    for i in range(n):
        if i % 2 == 0 and arr[i] % 2 != 0:
            wrong_even += 1
        elif i % 2 == 1 and arr[i] % 2 == 0:
            wrong_odd += 1

    if wrong_even == wrong_odd:
        return wrong_even
    else:
        return -1

# Read number of test cases
t = int(input())

# Process each test case
for _ in range(t):
    n = int(input())  # Length of array
    arr = list(map(int, input().split()))  # Read array
    print(min_swaps_to_good_array(n, arr))
