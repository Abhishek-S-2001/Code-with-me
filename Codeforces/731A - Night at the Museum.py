def min_rotations(s):
    current = 'a'
    total_moves = 0

    for char in s:
        clockwise = abs(ord(char) - ord(current))
        counterclockwise = 26 - clockwise
        total_moves += min(clockwise, counterclockwise)
        current = char  # Move to the new character

    return total_moves

# Example usage
s = input().strip()
print(min_rotations(s))
