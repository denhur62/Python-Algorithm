import sys
from collections import deque

while True:
    n, m = map(int, sys.stdin.readline().split())
    matrix = []
    dx = [0, 0, 1, -1, -1, -1, 1, 1]
    dy = [1, -1, 0, 0, -1, 1, -1, 1]
    if n == 0 and m == 0:
        break
    for _ in range(m):
        matrix.append(list(map(int, sys.stdin.readline().split())))

    visited = [[0]*n for _ in range(m)]
    queue = deque()
    count = 0
    for i in range(m):
        for j in range(n):
            if visited[i][j] == 0 and matrix[i][j] == 1:
                queue.append((j, i))
                visited[i][j] = 1
                count += 1
                while queue:
                    x, y = queue.popleft()
                    for k in range(8):
                        nx = dx[k]+x
                        ny = dy[k]+y
                        if 0 <= nx < n and 0 <= ny < m and visited[ny][nx] == 0 and matrix[ny][nx] == 1:
                            queue.append((nx, ny))
                            visited[ny][nx] = 1
    print(count)
