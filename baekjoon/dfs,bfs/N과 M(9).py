import sys
from itertools import permutations
n, m = map(int, input().split())
arr = list(map(int, sys.stdin.readline().split()))
arr = list(set(permutations(arr, m)))
arr.sort()
for i in arr:
    print(*i)
