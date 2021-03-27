import sys


N = int(input())
arr = list(map(int, input()))
cnt = 0


def check():
    for idx, val in enumerate(arr):
        if idx+1 < N and arr[idx] == arr[idx+1] == 0:
            return True
    return False


recur = [0]*51
recur[1] = 1
recur[2] = 1
for i in range(3, 51):
    recur[i] = recur[i-1]+recur[i-2]

answer = []
result = 1
if arr[0] == 0 or arr[-1] == 0 or check():
    print(0)
else:
    k = 0
    flag = 0
    for idx, val in enumerate(arr):
        if val == 0:
            temp = idx-k
            answer.append(recur[temp])
            k = idx+1
            flag = 1
        if idx == N-1:
            temp = idx-k+1
            answer.append(recur[temp])
    for i in answer:
        result *= i
    print(result)
