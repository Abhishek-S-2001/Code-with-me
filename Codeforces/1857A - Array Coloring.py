def can_color_array(arr):
    # If the total sum is odd, we need at least one odd and one even number
    has_odd = any(x % 2 != 0 for x in arr)
    has_even = any(x % 2 == 0 for x in arr)
    print(has_even, has_odd)
    if has_odd and has_even:
        return "YES"
    else:
        return "NO"

# Read input
t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    print(can_color_array(arr))