import sys
from itertools import combinations
a, b = map(int, sys.stdin.readline().split())

arr = []
for i in range(1, a+1):
    arr.append(i)

for i in combinations(arr, b):
    print(*i)
