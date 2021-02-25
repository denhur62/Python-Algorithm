import sys

N = int(input())
arr = list(map(int, sys.stdin.readline().split()))
M = max(arr)
minor = [True]*(M+1)
minor[1] = False
for i in range(2, int(M**0.5)+1):
    if minor[i] == True:
        for j in range(i+i, M+1, i):
            minor[j] = False
cnt = 0
for i in arr:
    if minor[i] == True:
        cnt += 1
print(cnt)
