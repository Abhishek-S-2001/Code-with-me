import math

#User function Template for python3

class Solution:    
    #Complete this function
    def printNos(self,N):
        #Your code here
        if N==0:
            return
        self.printNos(N-1)
        print(N,end=" ")
        
    # def ino(self,i,N):
    #     print(i, end=" ")
    #     if i != N:
    #         i=i+1
    #         self.ino(i,N)

    # def printNos(self,N):
    #     #Your code here
    #     i = 1
    #     self.ino(i,N)

#{ 
 # Driver Code Starts
#Initial Template for Python 3

def main():
    
    T=int(input())
    
    while(T>0):  
        N=int(input())
        
        ob=Solution()
        
        ob.printNos(N)
        print()
        T-=1

if __name__=="__main__":
    main()
# } Driver Code Ends