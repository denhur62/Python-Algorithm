from itertools import combinations
import sys

while True:
    arr = list(map(int, (sys.stdin.readline().split())))
    if arr[0] == 0:
        break
    else:
        N = arr[0]
        arr = arr[1:]
        for i in combinations(arr, 6):
            print(*i)
        print()
