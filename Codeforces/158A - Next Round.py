n , k = list(map(int, input().split()))
scores  = list(map(int, input().split()))
minScore = scores[k-1]
count = 0
for i in range(n):
    if scores[i] > 0 and scores[i] >= minScore:
        count += 1

print(count)