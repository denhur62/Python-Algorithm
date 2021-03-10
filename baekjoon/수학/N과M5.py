import sys
from itertools import combinations

a, b = map(int, sys.stdin.readline().split())

arr = []
arr += list(map(int, sys.stdin.readline().split()))
arr.sort()

for i in combinations(arr, b):
    print(*i)
