def find_max_k(x, y, n):
    m = (n - y) // x
    return m * x + y

t = int(input())
for _ in range(t):
    x, y, n = map(int, input().split())
    print(str(find_max_k(x, y, n)))