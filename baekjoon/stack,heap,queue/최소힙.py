import heapq
import sys

N = int(input())
arr = []
for i in range(N):
    temp = int(sys.stdin.readline().rstrip())
    if temp == 0:
        if not arr:
            print(0)
        else:
            print(heapq.heappop(arr))
    else:
        heapq.heappush(arr, temp)
