import sys
from collections import defaultdict

n = int(input())
arr = defaultdict(lambda: [])
visited = [True]*(n+1)
visited[0] = False
m = int(input())


def dfs(start):
    stack = [start]
    cnt = 0
    while stack:
        end = stack.pop()
        for i in arr[end]:
            if visited[i] == True:
                visited[i] = False
                stack.append(i)
                cnt += 1
    return cnt-1


for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    arr[a].append(b)
    arr[b].append(a)
print(dfs(1))
