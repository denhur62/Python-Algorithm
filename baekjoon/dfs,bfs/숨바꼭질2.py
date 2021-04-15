from collections import deque
N, M = map(int, input().split())

visited = [[-1, 0] for _ in range(100001)]
visited[N][0] = 0
visited[N][1] = 1


def dfs(start):
    queue = deque()
    queue.append(start)
    while queue:
        s = queue.popleft()
        for i in (s+1, s-1, s*2):
            if 0 <= i <= 100000:
                if visited[i][0] == -1:
                    visited[i][0] = visited[s][0]+1
                    visited[i][1] = visited[s][1]
                    queue.append(i)
                elif visited[i][0] == visited[s][0]+1:
                    visited[i][1] += visited[s][1]
    return visited[M][0], visited[M][1]


f, c = dfs(N)
print(f)
print(c)
