import sys
from itertools import combinations
import copy


N, M = map(int, sys.stdin.readline().split())

arr = []
two = []
one = []
for _ in range(N):
    temp = list(map(int, sys.stdin.readline().split()))
    arr.append(temp)

for i in range(N):
    for j in range(N):
        if arr[i][j] == 2:
            two.append((i, j))
            arr[i][j] = 0
        if arr[i][j] == 1:
            one.append((i, j))
dis = []
for i in one:
    min_dis = []
    for k in combinations(two, M):
        cnt = float('inf')
        for kk in k:
            if abs(kk[0]-i[0])+abs(kk[1]-i[1]) < cnt:
                cnt = abs(kk[0]-i[0])+abs(kk[1]-i[1])
        min_dis.append(cnt)
    dis.append(min_dis)
new_list = list(map(list, zip(*dis)))
dis = list(map(lambda x: sum(x), new_list))
print(min(dis))
