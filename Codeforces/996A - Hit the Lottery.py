n = int(input())

bill_count = 0
if n >= 100:
    bill_count += n // 100
    n = n % 100
if n >= 20:
    bill_count += n // 20
    n = n % 20
if n >= 10:
    bill_count += n // 10
    n = n % 10
if n >= 5:
    bill_count += n // 5
    n = n % 5
if n >= 1:
    bill_count += n

print(bill_count)