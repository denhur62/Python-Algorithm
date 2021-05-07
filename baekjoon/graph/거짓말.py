import sys

N, M = map(int, sys.stdin.readline().split())
tp = list(map(int, sys.stdin.readline().split()))
tp = set(tp[1:])
arr = []
for i in range(M):
    arr.append(list(map(int, sys.stdin.readline().split()))[1:])
arr = list(map(set, arr))
answer, cnt = 0, 0
while(cnt < M):
    for i in arr:
        if i & tp:
            tp = tp | i
    cnt += 1
for i in arr:
    if not i & tp:
        answer += 1
print(answer)
