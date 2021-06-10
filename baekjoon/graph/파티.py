import sys
from collections import defaultdict
import heapq


def dijkstra(graph, start):
    dis = {i: float('inf') for i in graph}
    dis[start] = 0
    queue = []
    heapq.heappush(queue, [dis[start], start])
    while queue:
        cur_dis, cur_destni = heapq.heappop(queue)

        if dis[cur_destni] < cur_dis:
            continue
        for new_destni, new_dis in graph[cur_destni].items():
            distance = cur_dis + new_dis
            if distance < dis[new_destni]:
                dis[new_destni] = distance
                heapq.heappush(queue, [distance, new_destni])
    return dis


n, m, x = map(int, sys.stdin.readline().split())
dic = defaultdict(lambda: {})
for i in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    dic[a][b] = c
dis = dijkstra(dic, x)
answer = []
for i in range(1, n+1):
    if i == x:
        continue
    temp = dijkstra(dic, i)
    answer.append(temp[x]+dis[i])
print(max(answer))
