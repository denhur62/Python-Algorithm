import sys
from collections import deque
N, M = map(int, sys.stdin.readline().split())
arr = []
for i in range(M):
    arr.append(list(sys.stdin.readline().rstrip()))
start = []
for i in range(N):
    if arr[0][i] == 'c':
        start.append((0, i))
nx = [0, 1, -1]
ny = [1, 0, 0]


def dfs(s_y, s_x):
    visited = [[True]*N for _ in range(M)]
    stack = deque()
    stack.append((s_y, s_x, 0))
    visited[s_y][s_x] = False
    answer = []
    while stack:
        y, x, cnt = stack.popleft()
        if y == M-1:
            answer.append(cnt)
        else:
            for i in range(3):
                dx = nx[i]+x
                dy = ny[i]+y
                if 0 <= dx < N and 0 <= dy < M and arr[dy][dx] == '.' and visited[dy][dx] == True:
                    visited[dy][dx] = False
                    if i != 0:
                        stack.append((dy, dx, cnt+1))
                    else:
                        stack.append((dy, dx, cnt))
    if not answer:
        return -1
    else:
        return min(answer)


answer = float('inf')
for i in start:
    temp = dfs(i[0], i[1])
    if temp < answer and temp != -1:
        answer = temp
if answer == float('inf'):
    print(-1)
else:
    print(answer)
