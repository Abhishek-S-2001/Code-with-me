n, k = map(int, input().split())
time = (240 - k)
score = 0
required_time = 0
for i in range(1,n+1):
    if time < (i * 5):
        break
    time -= (i * 5)
    score += 1

print(score)