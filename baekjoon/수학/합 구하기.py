import sys


N = int(sys.stdin.readline().rstrip())
arr = list(map(int, sys.stdin.readline().split()))
sum_arr = [0]*N
sum_arr[0] = arr[0]
for i in range(1, N):
    sum_arr[i] = sum_arr[i-1]+arr[i]

M = int(sys.stdin.readline().rstrip())
for i in range(M):
    a, b = map(int, sys.stdin.readline().split())
    if a == b:
        print(arr[a-1])
    elif a == 1:
        print(sum_arr[b-1])
    else:
        print(sum_arr[b-1]-sum_arr[a-2])
