import sys
from itertools import combinations
N, M = map(int, input().split())
arr = list(map(int, sys.stdin.readline().split()))

cnt = 0
for i in combinations(arr, 3):
    sum_i = sum(i)
    if sum_i <= M and sum_i > cnt:
        cnt = sum_i
print(cnt)
