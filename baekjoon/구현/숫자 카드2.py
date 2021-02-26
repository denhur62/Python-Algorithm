import sys
from collections import Counter
N = int(input())
arr1 = Counter(map(int, sys.stdin.readline().split()))
M = int(input())
arr2 = list(map(int, sys.stdin.readline().split()))

for i in arr2:
    print(arr1[i], end=" ")
