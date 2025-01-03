k, n, w = map(int, input().split())
t_cost = 0
for i in range(1, w + 1):
    t_cost = t_cost + k * i

res = t_cost - n
if res > 0:
    print(res)
else:
    print(0)