t = int(input())
results = []

for _ in range(t):
    a, b = map(int, input().split())
    results.append(str(b - a))

print("\n".join(results))