from collections import deque
import sys
N, M = map(int, sys.stdin.readline().split())
ladder = []
for i in range(N+M):
    NN, MM = map(int, input().split())
    ladder.append((NN, MM))


def check(a, b):
    cnt = 0
    for i in b:
        if i[0] == a:
            return cnt
        cnt += 1
    return False


def dfs(start):
    queue = deque()
    answer = float('inf')
    queue.append((start, 0))
    visited = [False]*101
    while queue:
        s, c = queue.popleft()
        if s == 100:
            return c
        elif s > 100:
            continue
        else:
            for i in range(1, 7):
                if s+i <= 100:
                    c = check(s+i, ladder)
                    if c:
                        queue.append((ladder[c][1], c))
                    else:
                        queue.append((s+i, c+1))


print(dfs(1))
