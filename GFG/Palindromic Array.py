# Your task is to complete this function
# Function should return True/False or 1/0
def PalinArray(arr ,n):
    # Code here
    ans = 1
    for i in arr:
        no = i
        Reverse = 0
        while(i > 0):    
            Reminder = i %10    
            Reverse = (Reverse *10) + Reminder    
            i = i //10
        if no != Reverse:
            ans = 0
    return ans

#{ 
 # Driver Code Starts
# Driver Program
if __name__=='__main__':
    t=int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        if PalinArray(arr, n):
            print(1)
        else:
            print(0)
# Contributed By: Harshit Sidhwa

# } Driver Code Ends