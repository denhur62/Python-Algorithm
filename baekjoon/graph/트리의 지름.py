from collections import deque, defaultdict
from heapq import heappush, heappop
import sys
N = int(input())

arr = defaultdict(lambda: {})
for _ in range(N):
    a = list(map(int, sys.stdin.readline().split()))
    i = 0
    start = a[0]
    while i < len(a)-1:
        if i == 0:
            arr[start][a[i+1]] = a[i+2]
            arr[a[i+1]][start] = a[i+2]
            i += 3
        else:
            arr[start][a[i]] = a[i+1]
            arr[a[i]][start] = a[i+1]
            i += 2


def dijkstra(start):
    distance = {node: float('inf') for node in arr}
    distance[start] = 0
    q = []
    heappush(q, [distance[start], start])
    while q:
        cur_dis, vertex = heappop(q)
        if distance[vertex] < cur_dis:
            continue
        for end_vertex, end_dis in arr[vertex].items():
            weight = end_dis+cur_dis
            if weight < distance[end_vertex]:
                distance[end_vertex] = weight
                heappush(q, [weight, end_vertex])
    return distance


temp = dict(map(reversed, dijkstra(start).items()))
circle_end = temp[max(temp)]
temp = dijkstra(circle_end)
print(max(temp.values()))
