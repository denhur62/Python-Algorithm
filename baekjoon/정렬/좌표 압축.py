import sys

N = int(input())
arr = list(map(int, sys.stdin.readline().split()))
arr_set = list(set(arr))
arr_set.sort()
arr_dict = {}
for idx, val in enumerate(arr_set):
    arr_dict[val] = idx

for i in arr:
    print(arr_dict[i], end=' ')
