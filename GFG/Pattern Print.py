from re import M


def printPat(n):
    #Code here
    y = n
    x=n
    for i in range(x): 
        n=y
        for i in range(n):
            m=x
            while(m>0):
                print(n, end=" ")
                m -= 1
            n -= 1
        print("$", end="")
        x -= 1
    print()

#{ 
 # Driver Code Starts
if __name__=='__main__':
    t=int(input())
    for i in range(t):
        n= int(input())
        printPat(n)
# } Driver Code Ends