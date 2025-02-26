n = int(input())
h = 0
while (h * (h + 1) * (h + 2)) // 6 <= n:
    h += 1  
print(h - 1)