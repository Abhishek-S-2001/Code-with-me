#User function Template for python3

from audioop import avg


class Solution:
	def find_median(self, v):
		# Code here
            n = len(v)
            x = n//2
            v.sort()
            if n%2 == 0:
                ans = avg(v[x-1],v[x])
            else:
                ans = v[x]
            return ans

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		v = list(map(int,input().split())) 
		ob = Solution();
		ans = ob.find_median(v)
		print(ans)
# } Driver Code Ends