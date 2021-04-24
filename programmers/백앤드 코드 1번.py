import sys

q = int(input())
def lam(y, x): return x-y


for i in range(q):
    N, M = map(int, sys.stdin.readline().split())
    arr = set(map(int, sys.stdin.readline().split()))
    if N == 0:
        print(0)
        continue
    i = 1
    while(1):
        cnt = 0
        for j in arr:
            cnt += i//j
        if cnt >= N:
            print(i)
            break
        else:
            i += 1
