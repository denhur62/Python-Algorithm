import sys
from collections import deque
N = int(input())
graph = [[] for _ in range(N+1)]
visited = [False] * (N+1)
parent = [[] for _ in range(N+1)]
for _ in range(N-1):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

stack = [1]
while stack:
    start = stack.pop()
    for i in graph[start]:
        if not visited[i]:
            visited[i] = True
            stack += [i]
            parent[i] = [start]

for i in parent[2:]:
    print(*i)
