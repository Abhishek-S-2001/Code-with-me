n, m = map(int, input().split())
a = 0
for i in range(1, n+1):
    if i % 2 == 1:
        for _ in range(m):
            print("#", end='')
        print()
    else:
        if a == 0 :
            for _ in range(m - 1):
                print(".", end='')
            print('#')
            a = 1
        else:
            print('#', end='')
            for _ in range(m - 1):
                print(".", end='')
            a = 0
            print()
            