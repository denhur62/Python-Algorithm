import sys
from collections import deque
n, m = map(int, sys.stdin.readline().split())
visited = [0 for _ in range(100001)]
queue = deque()
queue.append((n, 0))
limit = 100001
max = limit
while queue:
    (x, y) = queue.popleft()
    if x == m:
        print(y)
        break
    if visited[x] == 0:
        visited[x] = 1
        if 0 <= x*2 < limit:
            queue.append((x*2, y+1))
        if 0 <= x+1 < limit:
            queue.append((x+1, y+1))
        if 0 <= x-1 < limit:
            queue.append((x-1, y+1))
