import sys
import math

def max_product_after_increment(n, arr):
    original_product = math.prod(arr)
    max_product = original_product

    for i in range(n):
        new_arr = arr[:]
        new_arr[i] += 1
        max_product = max(max_product, math.prod(new_arr))
    
    return max_product

t = int(sys.stdin.readline().strip())

for _ in range(t):
    n = int(sys.stdin.readline().strip())
    arr = list(map(int, sys.stdin.readline().split()))
    print(max_product_after_increment(n, arr))
