t = int(input().strip())

for _ in range(t):
    s = list(map(int, input().split()))

    # First match: s1 vs s2, Second match: s3 vs s4
    winner1 = max(s[0], s[1])
    winner2 = max(s[2], s[3])

    # Get the two highest skill levels
    top_two = sorted(s)[-2:]

    # Check if the two match winners are the highest skill players
    if {winner1, winner2} == set(top_two):
        print("YES")
    else:
        print("NO")
