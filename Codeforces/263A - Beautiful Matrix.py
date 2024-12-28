matrix = []
for i in range(5):
    matrix.append(list(map(int, input().split())))
x = 0
y = 0
for m in range(5):
    for n in range(5):
        if matrix[m][n] == 1:
            x, y = m, n
            break
count = abs(x - 2) + abs(y - 2)
print(count)