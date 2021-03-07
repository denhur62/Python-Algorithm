import sys

n, m = map(int, sys.stdin.readline().split())
arr = []
for i in range(n):
    arr.append(int(sys.stdin.readline().rstrip()))

cnt = 0
for i in range(len(arr)-1, -1, -1):
    if m >= arr[i]:
        cnt += m//arr[i]
        m = m % arr[i]
print(cnt)
