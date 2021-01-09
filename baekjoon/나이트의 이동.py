import sys
from collections import deque

N = int(input())
dx = [-1, -2, -2, -1, 1, 2, 2, 1]
dy = [2, 1, -1, -2, -2, -1, 1, 2]
for _ in range(N):
    M = int(input())
    visited = [[0]*M for _ in range(M)]
    start_y, start_x = map(int, input().split())
    end_y, end_x = map(int, input().split())
    queue = deque()
    queue.append((start_y, start_x))
    visited[start_y][start_x] = 1
    flag = 0
    while queue:
        (y, x) = queue.popleft()
        if y == end_y and x == end_x:
            print(visited[y][x]-1)
            break
        for i in range(8):
            nx = dx[i]+x
            ny = dy[i]+y
            if 0 <= nx < M and 0 <= ny < M and visited[ny][nx] == 0:
                queue.append((ny, nx))
                visited[ny][nx] = visited[y][x]+1
