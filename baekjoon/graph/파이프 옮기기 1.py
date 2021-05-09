import sys
N = int(sys.stdin.readline())
arr = []
for i in range(N):
    arr.append(list(map(int, sys.stdin.readline().split())))

cnt = 0


def dfs(y, x, pipe):
    global cnt
    if (y == N-1 and x == N-1):
        cnt += 1
    else:
        if pipe == 1:
            if x+1 < N and arr[y][x+1] != 1:
                dfs(y, x+1, 1)
            if x+1 < N and y+1 < N and arr[y][x+1] != 1 and arr[y+1][x] != 1 and arr[y+1][x+1] != 1:
                dfs(y+1, x+1, 3)
        elif pipe == 2:
            if y+1 < N and arr[y+1][x] != 1:
                dfs(y+1, x, 2)
            if x+1 < N and y+1 < N and arr[y+1][x] != 1 and arr[y][x+1] != 1 and arr[y+1][x+1] != 1:
                dfs(y+1, x+1, 3)
        else:
            if x+1 < N and arr[y][x+1] != 1:
                dfs(y, x+1, 1)
            if y+1 < N and arr[y+1][x] != 1:
                dfs(y+1, x, 2)
            if x+1 < N and y+1 < N and arr[y][x+1] != 1 and arr[y+1][x] != 1 and arr[y+1][x+1] != 1:
                dfs(y+1, x+1, 3)


dfs(0, 1, 1)
print(cnt)
