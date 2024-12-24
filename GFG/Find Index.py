#User function Template for python3

class Solution:
    def findIndex (self,a, N, key ):
        #code here.
        ans = [-1,-1]
        find = []
        for i in range(0,N):
            if a[i] == key:
                find.append(i)
        if find:
            ans[0] = find[0]
            ans[1] = find[-1]
        return ans

#{ 
 # Driver Code Starts
#Initial Template for Python 3


t=int(input())
for _ in range(0,t):
    n=int(input())
    a=list(map(int,input().split()))
    key=int(input())
    ob = Solution()
    ans=ob.findIndex(a, n, key )
    print(*ans)
    
# } Driver Code Ends