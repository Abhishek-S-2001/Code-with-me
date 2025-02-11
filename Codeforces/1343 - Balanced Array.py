t = int(input())
results = []

for _ in range(t):
    n = int(input())

    if (n // 2) % 2 == 1:
        results.append("NO")
    else:
        results.append("YES")
        even_numbers = [i * 2 for i in range(1, (n // 2) + 1)]
        odd_numbers = [i * 2 - 1 for i in range(1, (n // 2))]
        odd_numbers.append(sum(even_numbers) - sum(odd_numbers)) 
        results.append(" ".join(map(str, even_numbers + odd_numbers)))

print("\n".join(results))