from collections import defaultdict

t = int(input())

for _ in range(t):
    n = int(input())
    arr = map(int, input().split())
    
    freq = defaultdict(int)
    found = -1
    
    # Process array
    for num in arr:
        freq[num] += 1
        if freq[num] == 3:  # Break early
            found = num
            break

    print(str(found))

