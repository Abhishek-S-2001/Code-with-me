#User function Template for python3

from operator import length_hint


class Solution:
    def longest(self, names, n):
    	# code here
        length = 0
        for i in names:
            str_len = len(i)
            if str_len>length:
                length = str_len
                ans = i
        return ans
    	

#{ 
 # Driver Code Starts
#Initial Template for Python 3

def main():
    T = int(input())
    while(T > 0):
        n=int(input())
        names = []
        for i in range(n):
            names.append(input())
        ob = Solution()
        print(ob.longest(names, n))
        
        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends