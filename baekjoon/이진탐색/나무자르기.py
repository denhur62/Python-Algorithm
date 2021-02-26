import sys

N, M = map(int, input().split())
arr = list(map(int, sys.stdin.readline().split()))

max_tree = max(arr)
start, end = 0, max_tree
while start <= end:
    mid = (start+end)//2
    cnt = sum([i-mid if i > mid else 0 for i in arr])
    if cnt < M:
        end = mid-1
    else:
        answer = mid
        start = mid+1
print(answer)
