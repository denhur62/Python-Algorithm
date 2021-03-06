import sys

seek = int(input())
N = int(input())
arr = set()
if N != 0:
    arr = set(map(int, sys.stdin.readline().split()))
flag = 0
min_count = abs(seek-100)
for i in range(0, 1000000):
    temp = list(map(int, str(i)))
    flag = 0
    for j in temp:
        if j in arr:
            flag = 1
            break
    if flag == 0:
        min_count = min(len(str(i))+abs(seek-i), min_count)

print(min_count)
