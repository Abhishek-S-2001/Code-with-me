x = 0

t = int(input())
for i in range(t):
    operation = input()
    if operation == "X++" or operation == "++X":
        x += 1
    else:
        x -= 1

print(x)