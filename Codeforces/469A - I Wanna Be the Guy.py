n = int(input())

x = list(map(int, input().split()))
y = list(map(int, input().split()))

z = set(x[1:] + y[1:])

if len(z) == n:
    print("I become the guy.")
else:
    print("Oh, my keyboard!")