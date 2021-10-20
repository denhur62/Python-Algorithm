import sys

M , N =map(int,input().split())
matrix=[]
DP=[[0]*(N+1) for _ in range(M+1)]
for i in range(M):
    matrix.append(list(map(int,sys.stdin.readline().split())))
answer=0
for i in range(1,M+1):
    for j in range(1,N+1):
        if matrix[i-1][j-1]==0:
            DP[i][j]=min(DP[i-1][j],DP[i][j-1],DP[i-1][j-1])+1
        answer=max(answer,DP[i][j])
print(answer)
