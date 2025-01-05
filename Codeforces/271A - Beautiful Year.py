n = int(input())
t = n + 1
s = set(list(str(t)))
while len(s) != len(str(n)):
    t += 1
    s = set(list(str(t)))

print(t)