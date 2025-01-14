n = int(input())
s = set(input().upper())
alphabets = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
count = 0
for i in alphabets:
    if i in s:
        count += 1

if count == 26:
    print('YES')
else:
    print('NO')