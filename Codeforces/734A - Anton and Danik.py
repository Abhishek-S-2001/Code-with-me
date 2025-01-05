n = int(input())
s = input()
A_count = s.count('A')
D_count = s.count('D')

if A_count > D_count:
    print('Anton')
elif A_count < D_count:
    print('Danik')
else:
    print('Friendship')