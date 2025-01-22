x_arr = list(map(int, input().split()))
x_arr.sort()
dist = abs(x_arr[1] - x_arr[0]) + abs(x_arr[1] - x_arr[2])

print(dist)