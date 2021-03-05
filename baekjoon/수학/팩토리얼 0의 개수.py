import sys

sys.setrecursionlimit(10**6)
arr = [0]*501
arr[0], arr[1], arr[2] = 0, 1, 2

N = int(input())


def fac(n):
    if arr[n] != 0:
        return arr[n]
    else:
        arr[n] = fac(n-1)*n
        return arr[n]


fac(N)
cnt = 0
arr = list(str(arr[N]))
flag = 0
for i in range(len(arr)-1, -1, -1):
    if arr[i] == '0':
        cnt += 1
    else:
        flag = 1
        break
print(cnt) if flag == 1 else print(0)
