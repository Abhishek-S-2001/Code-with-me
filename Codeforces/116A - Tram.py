t = int(input())
tram = 0
capacity = 0
for i in range(t):
    x, y = map(int, input().split())
    tram = tram - x + y
    capacity = max(capacity, tram)

print(capacity)