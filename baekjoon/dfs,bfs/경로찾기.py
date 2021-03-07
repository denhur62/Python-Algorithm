import sys

N = int(input())
arr = []
for i in range(N):
    arr.append(list(map(int, sys.stdin.readline().split())))


def dfs(i):
    stack = [i]
    visited = [True]*N
    while stack:
        e = stack.pop()
        for k in range(N):
            if arr[e][k] == 1 and visited[k] == True:
                visited[k] = False
                stack.append(k)
                arr[i][k] = 1


for i in range(N):
    dfs(i)

for i in arr:
    print(*i)
