t = int(input())
for _ in range(t):
    s = list('codeforces')
    input_str = list(input())
    count = 0
    for i in range(len(s)):
        if s[i] != input_str[i]:
            count += 1
    
    print(count)