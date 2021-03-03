import sys
a = int(input())

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
# j가 x좌표

sys.setrecursionlimit(100000)


def dfs(i, j):
    visited[i][j] = False
    for k in range(4):
        nx = dx[k]+j
        ny = dy[k]+i
        if 0 <= ny < N and 0 <= nx < M:
            if visited[ny][nx] == True and arr[ny][nx] == 1:
                dfs(ny, nx)


for _ in range(a):
    M, N, K = map(int, sys.stdin.readline().split())
    arr = [[0]*M for _ in range(N)]
    visited = [[True]*M for _ in range(N)]
    cnt = 0

    for _ in range(K):
        c, r = map(int, sys.stdin.readline().split())
        arr[r][c] = 1
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1 and visited[i][j] == True:
                dfs(i, j)
                cnt += 1
    print(cnt)
