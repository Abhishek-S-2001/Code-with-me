def count_keypresses(x):
    d = int(str(x)[0]) 
    l = len(str(x))
    return (d - 1) * 10 + (l * (l + 1)) // 2

t = int(input())

for _ in range(t):
    x = int(input())
    print(count_keypresses(x))
