import sys
from collections import defaultdict
alpha = ['A', 'B', 'C', 'D', 'E']
dic = defaultdict(str)
arr = list(map(float, sys.stdin.readline().split()))
for i in range(5):
    dic[alpha[i]] = arr[i]
N, M = map(int, sys.stdin.readline().split())
arr1 = []
arr2 = []
y_arr = []
w_arr = []
o_arr = []
for i in range(N):
    arr1.append(list(sys.stdin.readline().rstrip()))
for i in range(N):
    arr2.append(list(sys.stdin.readline().rstrip()))

for i in range(N):
    for j in range(M):
        if arr1[i][j] == 'Y':
            y_arr.append((dic[arr2[i][j]], arr2[i][j], i, j))
        if arr1[i][j] == 'O':
            o_arr.append((dic[arr2[i][j]], arr2[i][j], i, j))
y_arr = sorted(y_arr, key=lambda x: (-x[0], x[2], x[3]))
o_arr = sorted(o_arr, key=lambda x: (-x[0], x[2], x[3]))
for i in y_arr:
    print(i[1], i[0], i[2], i[3])
for i in o_arr:
    print(i[1], i[0], i[2], i[3])
