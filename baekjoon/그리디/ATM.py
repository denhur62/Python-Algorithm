import sys

N = int(input())

arr = list(map(int, sys.stdin.readline().split()))
arr.sort()
cnt = [0]*N
cnt[0] = arr[0]
for i in range(1, N):
    cnt[i] = cnt[i-1]+arr[i]
print(sum(cnt))
