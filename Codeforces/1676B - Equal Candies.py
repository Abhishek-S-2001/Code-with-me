t = int(input())
for _ in range(t):
    n = int(input())
    candies = list(map(int, input().split())) 
    
    min_candies = min(candies)
    total_eaten = sum(c - min_candies for c in candies) 
    
    print(total_eaten)