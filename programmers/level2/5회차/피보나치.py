def solution(n):
    
    a=[0 for i in range(0,100001)]
    a[1]=1

    for i in range(2,n+1):
        a[i]=a[i-1]+a[i-2]
    return a[n]%1234567