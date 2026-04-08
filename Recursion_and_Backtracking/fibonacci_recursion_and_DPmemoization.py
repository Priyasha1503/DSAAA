

#print reverse of array using n-1 appraoch
#fin nth fibbonaci number
n=int(input())
dp=[-1]*(n+1)
dp[0] = 0
dp[1] = 1
def fib(x,n):
    if x==0 or x==1:
        return x
    if dp[x]!=-1:
        return dp[x]
    dp[x] = fib(x-1,n) + fib(x-2,n)
    return dp[x]

obj = fib(n,n)
print(obj)


#writing optimized function for thw whle input as well again from scratch
def fib2(x,n):
    n=int(input())
    dp=[-1]*(n+1)
    dp[0] = 0
    dp[1] = 1
    
