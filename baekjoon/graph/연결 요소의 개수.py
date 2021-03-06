import sys
from collections import defaultdict

vertex, edge = map(int, sys.stdin.readline().split())
arr = defaultdict(lambda: [])
for _ in range(edge):
    a, b = map(int, sys.stdin.readline().split())
    arr[a].append(b)
    arr[b].append(a)
visited = [True]*(vertex+1)


def dfs(start):
    stack = [start]
    visited[start] = False
    while stack:
        st = stack.pop()
        for i in arr[st]:
            if visited[i] == True:
                stack.append(i)
                visited[i] = False


cnt = 0
for i in range(1, vertex+1):
    if visited[i] == True:
        dfs(i)
        cnt += 1
print(cnt)
