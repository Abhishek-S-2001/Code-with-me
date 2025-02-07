def form_teams(n, skills):
    programmers, mathematicians, athletes = [], [], []
    
    # Categorize students by skill
    for i, skill in enumerate(skills):
        if skill == 1:
            programmers.append(i + 1)
        elif skill == 2:
            mathematicians.append(i + 1)
        else:
            athletes.append(i + 1)

    # Determine the maximum number of complete teams
    w = min(len(programmers), len(mathematicians), len(athletes))
    print(w)

    # Form teams
    for i in range(w):
        print(programmers[i], mathematicians[i], athletes[i])

# Input Handling
n = int(input())
skills = list(map(int, input().split()))

form_teams(n, skills)
