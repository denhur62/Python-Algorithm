import sys
from collections import deque

a, b = map(int, sys.stdin.readline().split())

visited = [True]*100001
visited[a] = False


def dfs(a, count):
    stack = deque()
    stack.append((a, count))
    answer = float('inf')
    while stack:
        idx, cnt = stack.popleft()
        if idx == b:
            answer = min(answer, cnt)
        else:
            for i in (idx+1, idx-1, 2*idx):
                if 0 <= i < 100001:
                    if visited[i] == True:
                        visited[i] = False
                        if i == 2*idx:
                            stack.appendleft((i, cnt))
                        else:
                            stack.append((i, cnt+1))
    return answer


print(dfs(a, 0))
