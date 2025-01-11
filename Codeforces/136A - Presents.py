n = int(input())
arr = list(map(int, input().split()))
new_arr = [0] * n
for i in range(n):
    temp = arr[i] - 1
    new_arr[temp] = str(i + 1)
new_arr = " ".join(new_arr)
print(new_arr)