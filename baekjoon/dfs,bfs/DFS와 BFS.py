import sys
from collections import deque
n, m, k = map(int, sys.stdin.readline().split())
matrix = [[0]*(n+1) for _ in range(n+1)]
for _ in range(m):
    start, end = map(int, sys.stdin.readline().split())
    matrix[start][end] = 1
    matrix[end][start] = 1


def bfs(queue, visited):
    while queue:
        start = queue.popleft()
        for i in range(1, n+1):
            if matrix[start][i] == 1 and i not in visited:
                queue += [i]
                visited += [i]
    return visited


def dfs(start, queue):
    for i in range(1, n+1):
        if matrix[start][i] == 1 and i not in queue:
            queue += [i]
            dfs(i, queue)
    return queue


print(*dfs(k, [k]))
q = deque()
q += [k]
print(*bfs(q, [k]))
