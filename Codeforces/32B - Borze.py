def decode_borze(code):
    result = ""
    i = 0
    
    while i < len(code):
        if code[i] == '.':  # '0' in ternary
            result += '0'
        elif i + 1 < len(code) and code[i] == '-' and code[i+1] == '.':  # '1'
            result += '1'
            i += 1  # Skip next character
        elif i + 1 < len(code) and code[i] == '-' and code[i+1] == '-':  # '2'
            result += '2'
            i += 1  # Skip next character
        i += 1
    
    return result

# Example usage
borze_code = input().strip()
print(decode_borze(borze_code))
