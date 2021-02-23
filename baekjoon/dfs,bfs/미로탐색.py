import sys
from collections import deque
n, m = map(int, sys.stdin.readline().split())
matrix = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(n)]
visited = [[0 for _ in range(m)] for _ in range(n)]
dx = [0, 1, -1, 0]
dy = [-1, 0, 0, 1]

queue = deque()
queue.append((0, 0))
while queue:
    (y, x) = queue.popleft()
    if x == m-1 and y == n-1:
        print(visited[y][x]+1)
    for i in range(4):
        nx = dx[i]+x
        ny = dy[i]+y
        if 0 <= ny < n and 0 <= nx < m and matrix[ny][nx] == 1 and visited[ny][nx] == 0:
            visited[ny][nx] = visited[y][x]+1
            queue.append((ny, nx))
