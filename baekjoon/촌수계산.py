import sys
from collections import deque
N = int(input())
find_a, find_b = map(int, input().split())
M = int(input())
matrix = [[0]*(N+1) for _ in range(N+1)]
visited = [False]*(N+1)

for _ in range(M):
    a, b = map(int, input().split())
    matrix[a][b] = 1
    matrix[b][a] = 1


def bfs(count):
    while queue:
        x, y = queue.popleft()
        for i in range(1, N+1):
            if i == find_b and matrix[x][i] == 1:
                return y+1
            if matrix[x][i] == 1 and visited[i] == False:
                visited[i] = True
                queue.append((i, y+1))
                count += 1
    return -1


queue = deque()
queue.append((find_a, 0))
visited[find_a] = True
if find_a == find_b:
    print(0)
else:
    print(bfs(0))
