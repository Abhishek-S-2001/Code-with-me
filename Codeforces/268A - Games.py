n = int(input())
teams = []
for i in range(n):
    teams.append(list(map(int, input().split())))

games = []
for i in range(n):
    for j in range(n):
        if i != j:
            games.append((teams[i], teams[j]))
count = 0
for game in games:
    if game[0][0] == game[1][1]:
        count += 1
    
print (count)