import sys

N = int(input())
arr = list(map(int, sys.stdin.readline().split()))
arr.sort()
M = int(input())
arr2 = list(map(int, sys.stdin.readline().split()))


def binary_search(answer):
    start, end = 0, N-1
    while start <= end:
        mid = (start+end)//2
        if arr[mid] == answer:
            return 1
        elif arr[mid] < answer:
            start = mid+1
        else:
            end = mid-1
    return 0


for i in arr2:
    print(binary_search(i))
