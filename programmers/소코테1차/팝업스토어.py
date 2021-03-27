import sys
from collections import deque
N, M = map(int, sys.stdin.readline().split())
arr = []
for i in range(M):
    arr.append(list(map(int, sys.stdin.readline().split())))
DP = [[0]*N for _ in range(M)]
for i in range(N):
    if i == 0:
        DP[0][i] = arr[0][0]
    else:
        DP[0][i] = arr[0][i]+DP[0][i-1]
for i in range(1, M):
    DP[i][0] = arr[i][0]+DP[i-1][0]
for i in range(1, M):
    for j in range(1, N):
        DP[i][j] = max(DP[i-1][j], DP[i][j-1])+arr[i][j]

print(DP[M-1][N-1])
