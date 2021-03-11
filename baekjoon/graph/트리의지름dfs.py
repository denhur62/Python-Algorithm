import sys
from collections import defaultdict, deque

N = int(input())
dic = defaultdict(lambda: {})


def dfs(start):
    stack = deque()
    stack.append((0, start))
    visited = [True]*(N+1)
    visited[start] = False
    distance = 0
    node = 0
    while stack:
        d, s = stack.popleft()
        for i in dic[s].items():
            end, dis = i
            if visited[end] == True:
                visited[end] = False
                if distance < dis+d:
                    distance = dis+d
                    node = end
                    stack.append((distance, end))
                else:
                    stack.append((dis+d, end))
    return [node, distance]


for i in range(N-1):
    a, b, c = map(int, sys.stdin.readline().split())
    dic[a][b] = c
    dic[b][a] = c

temp = dfs(1)
answer = dfs(temp[0])
print(answer[1])
