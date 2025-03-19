t = int(input().strip())  # Read number of test cases

for _ in range(t):
    n = int(input().strip())  # Read number of columns
    row1 = input().strip()  # First row
    row2 = input().strip()  # Second row
    
    # Transform G and B into X
    row1_transformed = row1.replace('G', 'X').replace('B', 'X')
    row2_transformed = row2.replace('G', 'X').replace('B', 'X')
    
    # Check if both rows are the same after transformation
    if row1_transformed == row2_transformed:
        print("YES")
    else:
        print("NO")
