def fibonacciNumber(n):
    # Write your code here.
    mod=(10**9)+7
    a=0 
    b=1
    for i in range(2,n+1):
        c=(a+b)%mod
        a=b
        b=c
    return b%mod

    




