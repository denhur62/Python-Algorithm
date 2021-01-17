import sys
from collections import deque

N, M = map(int, input().split())
Matrix = [list(map(int, sys.stdin.readline().rstrip()))
          for _ in range(N)]
visit = [[[0] * 2 for i in range(M)] for i in range(N)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
queue = deque()
queue.append((0, 0, 0))


def bfs():
    while queue:
        (y, x, z) = queue.popleft()
        if y == N-1 and x == M-1:
            return visit[y][x][z]+1
        for i in range(4):
            ny = y+dy[i]
            nx = x+dx[i]
            if 0 <= nx < M and 0 <= ny < N and Matrix[ny][nx] == 0 and visit[ny][nx][z] == 0:
                visit[ny][nx][z] = visit[y][x][z]+1
                queue.append((ny, nx, z))
            if 0 <= nx < M and 0 <= ny < N and Matrix[ny][nx] == 1 and z == 0:
                visit[ny][nx][1] = visit[y][x][z]+1
                queue.append((ny, nx, 1))
    return -1


print(bfs())
