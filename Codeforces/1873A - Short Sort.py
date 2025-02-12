t = int(input())
for _ in range(t):
    s = list(input())
    temp = []
    fs = ['a', 'b', 'c']
    for i in range(len(s)):
        if s[i] == fs[i]:
            temp.append(0)
        else:
            temp.append(1)
    if temp.count(1) == 3:
        print('NO')
    else:
        print('YES')
