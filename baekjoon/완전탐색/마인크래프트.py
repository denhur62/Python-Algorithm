import sys
from collections import Counter

N, M, inven = map(int, sys.stdin.readline().split())
arr = []
for i in range(N):
    arr += (list(map(int, sys.stdin.readline().split())))
arr = Counter(arr)
time_answer = float('inf')
floor_answer = 0
for floor in range(257):
    cnt_inven = 0
    time = 0
    for i in arr:
        if i > floor:
            time += 2*(i-floor)*arr[i]
            cnt_inven += (i-floor)*arr[i]
        else:
            time += (floor-i)*arr[i]
            cnt_inven += (i-floor)*arr[i]
    if cnt_inven+inven >= 0 and time_answer >= time:
        time_answer = time
        floor_answer = floor
print(time_answer, floor_answer)
