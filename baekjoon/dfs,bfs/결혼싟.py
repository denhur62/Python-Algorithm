import sys
from collections import deque

N = int(input())
matrix = [[0]*(N+1) for _ in range(N+1)]
visited = [0]*(N+1)
M = int(input())
queue = deque()
count = 0

for i in range(M):
    start_y, start_x = map(int, sys.stdin.readline().split())
    matrix[start_y][start_x] = 1
    matrix[start_x][start_y] = 1
visited[1] = 1
for i in range(1, 2):
    for j in range(1, N+1):
        if matrix[i][j] == 1 and visited[j] == 0:
            queue.append((i, j))
            visited[j] = 1
            count += 1

while queue:
    (y, x) = queue.popleft()
    for i in range(1, N+1):
        if matrix[x][i] == 1 and visited[i] == 0:
            visited[i] = 1
            count += 1
print(count)
