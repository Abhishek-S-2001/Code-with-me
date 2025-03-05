t = int(input().strip())

for _ in range(t):
    n = int(input().strip())
    a = list(map(int, input().split()))

    max_blank_space = 0
    current_blank_space = 0

    for num in a:
        if num == 0:
            current_blank_space += 1
            max_blank_space = max(max_blank_space, current_blank_space)
        else:
            current_blank_space = 0

    print(max_blank_space)
