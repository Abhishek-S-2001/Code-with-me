#function should return an integer
#your task is to compplete this function
class Solution:
    def convertFive(self,n):
        #Code here
        arr1 = list(map(int, str(n)))
        for i in range(len(arr1)):
            if arr1[i] == 0:
                arr1[i] = 5

        s = [str(i) for i in arr1]
        ans = int("".join(s))
        return ans
        

#{ 
 # Driver Code Starts
if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n=int(input())
        print(Solution().convertFive(n))
# Contributed by: Harshit sidhwa

# } Driver Code Ends