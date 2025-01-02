n = int(input())
r = n % 5
if r == 0:
    res = n // 5
else:
    res = (n // 5) + 1

print(res)
