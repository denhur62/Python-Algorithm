import sys
from heapq import heappush, heappop

N = int(input())
arr = []
count = 0
for _ in range(N):
    temp = list(map(int, sys.stdin.readline().split()))
    for i in temp:
        if count >= N:
            heappush(arr, i)
            heappop(arr)
        else:
            count += 1
            heappush(arr, i)

print(min(arr))
