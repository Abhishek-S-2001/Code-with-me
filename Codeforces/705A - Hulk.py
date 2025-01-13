n = int(input())
res = 'I hate '

for i in range(2, n+1):
    res += 'that '
    if i % 2 == 0:
        res += 'I love '
    else:
        res += 'I hate '

print(res + 'it')