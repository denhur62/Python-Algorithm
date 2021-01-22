import heapq
import sys

queue = []
N = int(input())
for i in range(N):
    m = int(sys.stdin.readline())
    if m == 0:
        if queue:
            Max = heapq.heappop(queue)
            print(-Max)
        else:
            print("0")
    else:
        heapq.heappush(queue, -m)
