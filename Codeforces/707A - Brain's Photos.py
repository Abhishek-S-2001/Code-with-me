# Read the input values for n and m
n, m = map(int, input().split())

# Define the colored pixels
colored_pixels = {'C', 'M', 'Y'}

# Flag to determine if the image is colored
is_colored = False

# Iterate over the rows
for _ in range(n):
    row = input().split()  # Read the row and split it into characters
    if any(pixel in colored_pixels for pixel in row):
        is_colored = True
        break  # Exit early if a colored pixel is found

# Print the result
print("#Color" if is_colored else "#Black&White")
