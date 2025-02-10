def find_winner(n, rounds):
    mishka_wins = 0
    chris_wins = 0

    for m, c in rounds:
        if m > c:
            mishka_wins += 1
        elif m < c:
            chris_wins += 1

    if mishka_wins > chris_wins:
        print("Mishka")
    elif chris_wins > mishka_wins:
        print("Chris")
    else:
        print("Friendship is magic!^^")

# Read input
n = int(input())  # Number of rounds
rounds = [tuple(map(int, input().split())) for _ in range(n)]

# Process and print the result
find_winner(n, rounds)
