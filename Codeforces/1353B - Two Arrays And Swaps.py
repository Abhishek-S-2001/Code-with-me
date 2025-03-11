t = int(input())  # Number of test cases

for _ in range(t):
    n, k = map(int, input().split())  # Read n and k
    a = list(map(int, input().split()))  # Read array a
    b = list(map(int, input().split()))  # Read array b
    
    a.sort()  # Sort a in ascending order
    b.sort(reverse=True)  # Sort b in descending order

    # Perform swaps up to k times
    for i in range(k):
        if b[i] > a[i]:  # Swap if it increases sum
            a[i], b[i] = b[i], a[i]
        else:
            break  # No further beneficial swaps possible
    
    print(sum(a))  # Output the maximum sum of a
