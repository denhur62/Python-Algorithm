from collections import deque, defaultdict
import sys
N, M = map(int, sys.stdin.readline().split())
ladder = defaultdict(int)
for i in range(N+M):
    NN, MM = map(int, sys.stdin.readline().split())
    ladder[NN] = MM


def dfs(start):
    queue = deque()
    answer = float('inf')
    queue.append((start, 0))
    visited = [False]*101
    while queue:
        s, c = queue.popleft()
        if s == 100:
            return c
        else:
            for i in range(1, 7):
                ns = s+i
                if ns <= 100:
                    if ladder[ns] != 0 and visited[ladder[ns]] == False:
                        visited[ladder[ns]] == True
                        queue.append((ladder[ns], c+1))
                    elif visited[ns] == False:
                        visited[ns] == True
                        queue.append((ns, c+1))


print(dfs(1))
