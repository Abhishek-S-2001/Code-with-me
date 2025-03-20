def min_changes_to_make_good_matrix():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    index = 0
    t = int(data[index])  # Number of test cases
    index += 1
    results = []
    
    for _ in range(t):
        n, m = map(int, (data[index], data[index+1]))
        index += 2
        matrix = [data[i] for i in range(index, index + n)]
        index += n
        
        row_xor = [0] * n
        col_xor = [0] * m
        
        # Compute XOR for each row and column
        for i in range(n):
            for j in range(m):
                val = int(matrix[i][j])
                row_xor[i] ^= val
                col_xor[j] ^= val
        
        # Count invalid rows and columns
        invalid_rows = sum(1 for x in row_xor if x != 0)
        invalid_cols = sum(1 for x in col_xor if x != 0)
        
        # Minimum number of changes required
        results.append(str(max(invalid_rows, invalid_cols)))
    
    sys.stdout.write("\n".join(results) + "\n")

