import sys
import collections

n = int(sys.stdin.readline())
arr = [list(map(int, str(input())))for i in range(n)]
visited = [[0 for i in range(n)] for j in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]


def dfs(x, y):
    global cnt
    visited[x][y] = 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            if visited[nx][ny] == 0 and arr[nx][ny] == 1:
                cnt += 1
                dfs(nx, ny)
    return cnt


cnt = 1
cntlist = []
for a in range(n):
    for b in range(n):
        if arr[a][b] == 1 and visited[a][b] == 0:
            cnt = dfs(a, b)
            cntlist.append(cnt)
            cnt = 1

print(len(cntlist))
for n in sorted(cntlist):
    print(n)
