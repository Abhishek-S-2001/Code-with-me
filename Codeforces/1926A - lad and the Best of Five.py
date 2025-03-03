def most_frequent_letter(s):
    return 'A' if s.count('A') > s.count('B') else 'B'

t = int(input().strip())

for _ in range(t):
    s = input().strip()
    print(most_frequent_letter(s))
