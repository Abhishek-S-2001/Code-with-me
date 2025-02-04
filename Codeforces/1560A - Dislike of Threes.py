def generate_polycarp_sequence(limit=1000):
    sequence = []
    num = 1
    while len(sequence) < limit:
        if num % 3 != 0 and num % 10 != 3:
            sequence.append(num)
        num += 1
    return sequence

def solve():
    t = int(input())
    sequence = generate_polycarp_sequence(1000)
    for _ in range(t):
        k = int(input())
        print(sequence[k - 1])

# Example usage
solve()
