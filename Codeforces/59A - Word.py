word = input()
l, u = 0, 0
for i in word:
    if i.isupper():
        u += 1
    else:
        l += 1
if u > l:
    print(word.upper())
else:
    print(word.lower())