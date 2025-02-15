def is_prime(num):
    """Returns True if num is a prime number, else False."""
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def next_prime(n):
    """Returns the next prime number after n."""
    num = n + 1
    while not is_prime(num):
        num += 1
    return num

# Read input values
n, m = map(int, input().split())

# Find next prime after n
expected_prime = next_prime(n)

# Compare and print result
if expected_prime == m:
    print("YES")
else:
    print("NO")
