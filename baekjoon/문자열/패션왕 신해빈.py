import sys
from collections import defaultdict
N = int(input())

for _ in range(N):
    M = int(input())
    arr = defaultdict(lambda: [])
    for _ in range(M):
        a, b = sys.stdin.readline().split()
        arr[b].append(a)
    cnt = 1
    for i in arr:
        cnt *= len(arr[i])+1
    print(cnt-1)
