from collections import defaultdict
import sys
import heapq
N = int(input())
M = int(input())
dic = [[] for _ in range(N+1)]
for _ in range(M):
    a, b, c = map(int, sys.stdin.readline().split())
    dic[a].append((b, c))
start, end = map(int, sys.stdin.readline().split())


def dijstra(s):
    distance = {node: float('inf') for node in range(N+1)}
    distance[s] = 0
    queue = []
    heapq.heappush(queue, [distance[s], s])
    while queue:
        cur_distance, cur_vertex = heapq.heappop(queue)
        if distance[cur_vertex] < cur_distance:
            continue
        for end_vertex, weight in dic[cur_vertex]:
            dis = cur_distance+weight
            if dis < distance[end_vertex]:
                distance[end_vertex] = dis
                heapq.heappush(queue, [dis, end_vertex])
    return distance


print(dijstra(start)[end])
