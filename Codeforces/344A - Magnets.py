n = int(input())
count = 0
a = 0
for i in range(n):
    m = input()
    if m != a:
        count += 1
        a = m
print(count)