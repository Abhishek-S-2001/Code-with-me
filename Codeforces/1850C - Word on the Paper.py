t = int(input())

for _ in range(t):
    str1 = ''
    for _ in range(8):
        s = input()
        for i in s:
            if i != '.':
                str1 += i

    print(str1)