import sys

N,M=map(int,sys.stdin.readline().split())

arr=list(map(int,sys.stdin.readline().split()))
DP=[0]*(N+1)
DP[0]=0
DP[1]=arr[0]
for i in range(2,N+1):
    DP[i]=arr[i-1]+DP[i-1]
for i in range(M):
    x,y=map(int,sys.stdin.readline().split())
    print(DP[y]-DP[x-1])