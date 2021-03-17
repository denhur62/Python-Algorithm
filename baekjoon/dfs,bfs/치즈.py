import sys

N, M = map(int, sys.stdin.readline().split())

arr = []
for _ in range(N):
    arr.append(list(map(int, sys.stdin.readline().split())))

ny = [1, -1, 0, 0]
nx = [0, 0, 1, -1]


def dfs(i, j):
    visited[i][j] = False
    stack = [(i, j)]
    temp = []
    while stack:
        y, x = stack.pop()
        for k in range(4):
            dy = ny[k]+y
            dx = nx[k]+x
            if 0 <= dy < N and 0 <= dx < M:
                if arr[dy][dx] >= 1:
                    arr[dy][dx] += 1
                if arr[dy][dx] == 0 and visited[dy][dx] == True:
                    visited[dy][dx] = False
                    stack.append((dy, dx))
    return temp


all_zero = False
answer = 0
while not all_zero:
    all_zero = True
    visited = [[True]*M for _ in range(N)]

    dfs(0, 0)
    for i in range(N):
        for j in range(M):
            if arr[i][j] >= 3:
                all_zero = False
                arr[i][j] = 0
            if 1 <= arr[i][j] <= 2:
                arr[i][j] = 1
    answer += 1

print(answer-1)
