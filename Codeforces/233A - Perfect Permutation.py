n = int(input())

if n % 2 == 1:
    print(-1)
else:
    permutation = []
    for i in range(1, n+1, 2):
        permutation.append(i+1)
        permutation.append(i)
    print(*permutation)