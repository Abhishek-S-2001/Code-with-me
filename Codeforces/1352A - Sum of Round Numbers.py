# Read the number of test cases
t = int(input())

# Process each test case
for _ in range(t):
    # Read the number n
    n = int(input())
    
    round_numbers = []
    place_value = 1  # To track the place (ones, tens, hundreds, etc.)
    
    # Traverse through each digit of the number
    while n > 0:
        digit = n % 10
        if digit != 0:
            round_numbers.append(digit * place_value)
        n //= 10
        place_value *= 10  # Move to the next place
    
    # Output the result
    print(len(round_numbers), *round_numbers)
