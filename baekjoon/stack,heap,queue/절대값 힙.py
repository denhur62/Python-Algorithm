import sys
from heapq import heappush, heappop

N = int(input())
arr = []
for i in range(N):
    temp = int(sys.stdin.readline().rstrip())
    if temp == 0:
        if not arr:
            print(0)
        else:
            answer = heappop(arr)
            print(answer[1])
    else:
        heappush(arr, [abs(temp), temp])
