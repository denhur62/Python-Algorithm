import sys
from collections import deque
n = int(input())
m = [list(map(str, input())) for _ in range(n)]
visited = [[0 for _ in range(n)] for _ in range(n)]
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]


def bfs(queue, visited):
    while queue:
        [y, x] = queue.popleft()
        color = m[y][x]
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0 <= nx < n and 0 <= ny < n and visited[ny][nx] == 0 and color == m[ny][nx]:
                queue.append([ny, nx])
                visited[ny][nx] = 1


def bfs2(queue, visited):
    while queue:
        [y, x] = queue.popleft()
        color = m[y][x]
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if color in 'RG':
                if 0 <= nx < n and 0 <= ny < n and visited[ny][nx] == 0 and m[ny][nx] in 'RG':
                    queue.append([ny, nx])
                    visited[ny][nx] = 1
            else:
                if 0 <= nx < n and 0 <= ny < n and visited[ny][nx] == 0 and color == m[ny][nx]:
                    queue.append([ny, nx])
                    visited[ny][nx] = 1


queue = deque()
answer1 = 0
for i in range(n):
    for j in range(n):
        if visited[i][j] == 0:
            queue.append([i, j])
            visited[i][j] = 1
            bfs(queue, visited)
            answer1 += 1
visited = [[0 for _ in range(n)] for _ in range(n)]
answer2 = 0
for i in range(n):
    for j in range(n):
        if visited[i][j] == 0:
            queue.append([i, j])
            visited[i][j] = 1
            bfs2(queue, visited)
            answer2 += 1
print(answer1, answer2)
