import sys
N, M = map(int, input().split())

arr = list(map(int, sys.stdin.readline().split()))

start, end = 0, 0
cnt = 0
answer = 0
for start in range(N):
    while cnt < M and end < N:
        cnt += arr[end]
        end += 1
    if cnt == M:
        answer += 1
    cnt -= arr[start]
print(answer)
