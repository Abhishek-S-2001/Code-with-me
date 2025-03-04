import sys

t = int(input().strip())

for _ in range(t):
    expression = input().strip()
    print(eval(expression))
