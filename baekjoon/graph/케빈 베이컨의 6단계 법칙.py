from heapq import heappush, heappop
from collections import defaultdict
import sys

v, e = map(int, input().split())

graph = defaultdict(lambda: {})


def dijkstra(start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    queue = []
    heappush(queue, [distances[start], start])
    while queue:
        cur_distance, cur_vertex = heappop(queue)
        if distances[cur_vertex] < cur_distance:
            continue
        for vertex, weight in graph[cur_vertex].items():
            dis = cur_distance+weight
            if dis < distances[vertex]:
                distances[vertex] = dis
                heappush(queue, [dis, vertex])
    return distances


for i in range(e):
    a, b = map(int, sys.stdin.readline().split())
    graph[a][b] = 1
    graph[b][a] = 1
large = float('inf')
answer = 0
for i in range(1, v+1):
    arr = dijkstra(i)
    temp = sum(arr.values())
    if large > temp:
        large = temp
        answer = i
print(answer)
