t = int(input())  # Number of test cases

for _ in range(t):
    n = int(input())  # Number of candies
    candies = list(map(int, input().split()))  # List of candy weights
    
    count1 = candies.count(1)  # Count of 1-gram candies
    count2 = candies.count(2)  # Count of 2-gram candies
    total_sum = count1 + 2 * count2  # Total weight of candies

    if total_sum % 2 != 0:
        print("NO")  # Odd sum cannot be split equally
    else:
        if count1 > 0 or count2 % 2 == 0:
            print("YES")  # Possible to split fairly
        else:
            print("NO")  # Only 2s and odd count → Not possible
