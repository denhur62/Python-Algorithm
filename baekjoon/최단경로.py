from collections import defaultdict
from heapq import heappush, heappop
import sys


def dijkstra(distance, start, M):
    graph = {v: float('inf') for v in range(1, M+1)}
    graph[start] = 0
    queue = []
    heappush(queue, [graph[start], start])
    while queue:
        cur_dist, cur_vertex = heappop(queue)
        if cur_dist > graph[cur_vertex]:
            pass
        for next_vertex, weight in distance[cur_vertex].items():
            dist = weight+cur_dist
            if dist < graph[next_vertex]:
                graph[next_vertex] = dist
                heappush(queue, [dist, next_vertex])
    return graph


M, N = map(int, sys.stdin.readline().split(' '))
start = int(input())
graph = defaultdict(lambda: {})
for i in range(N):
    a, b, c = map(int, sys.stdin.readline().split(' '))
    if b in graph[a]:
        if graph[a][b] > c:
            graph[a][b] = c
    else:
        graph[a].update({b: c})
result = dijkstra(graph, start, M)
print(result)
for i in range(1, M+1):
    print("INF") if result[i] == float('inf') else print(result[i])
