n = int(input())
count = 0
for i in range(n):
    x = input()
    count_1 = x.count("1")
    if count_1 > 1:
        count += 1

print(count)