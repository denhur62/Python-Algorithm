import sys
from collections import deque

sys.setrecursionlimit(100000)

N = int(sys.stdin.readline().strip())
matrix = [list(map(int, sys.stdin.readline().split())) for i in range(N)]
shark = []
fish_coordinates = []
fish = [1, 2, 3, 4, 5, 6]
shark_size = 2
shark_count = 0
for idx, ival in enumerate(matrix):
    for jdx, jval in enumerate(ival):
        if(jval == 9):
            matrix[idx][jdx] = 0
            shark += [idx, jdx, 0]
dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]
queue = deque()
answer = 0
count = 0
while True:
    enable = 0
    enable_fish = []
    if shark_size == shark_count:
        shark_size += 1
        shark_count = 0
        break
    queue.append(shark)
    visited = [[0 for i in range(N)] for j in range(N)]
    while queue:
        x, y, count = queue.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0 <= nx < N and 0 <= ny < N and matrix[nx][ny] != 0 and matrix[nx][ny] < shark_size and visited[nx][ny] == 0:
                enable_fish.append([nx, ny, count])
            if 0 <= nx < N and 0 <= ny < N and (matrix[nx][ny] == 0 or matrix[nx][ny] == shark_size) and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                queue.append([nx, ny, count+1])

    if not enable_fish:
        break
    enable_fish = sorted(enable_fish, key=lambda x: (x[2], x[0], x[1]))
    nx, ny, nc = enable_fish[0]
    matrix[nx][ny] = 0
    shark_count += 1
    answer += nc+1
    count = 0
    shark = [nx, ny, 0]
print(answer)


sys.stdin.readline()
