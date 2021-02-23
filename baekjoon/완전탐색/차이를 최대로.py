from itertools import permutations
import sys


def gap(arr):
    count = 0
    for i in range(len(arr)-1):
        count += abs(arr[i]-arr[i+1])
    return count


N = int(input())
arr = list(map(int, (sys.stdin.readline().split())))

a = list(map(gap, permutations(arr, N)))
print(max(a))
