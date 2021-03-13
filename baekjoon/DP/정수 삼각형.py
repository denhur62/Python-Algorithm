import sys

N = int(input())
matrix = [[0]*N for _ in range(N)]
DP = [[0]*(N) for _ in range(N)]
k = 0
for i in range(1, N+1):
    a = list(map(int, sys.stdin.readline().split()))
    for j in range(i):
        matrix[k][j] = a[j]
    k += 1
DP[0][0] = matrix[0][0]
for i in range(1, N):
    DP[i][0] = matrix[i][0]+DP[i-1][0]
    for j in range(1, N):
        DP[i][j] = matrix[i][j]+max(DP[i-1][j-1], DP[i-1][j])
print(max(DP[-1]))
