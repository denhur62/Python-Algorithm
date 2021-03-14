from collections import deque

N, M = map(int, input().split())
max_q = 1000000000
q = deque()
flag = 0
q.append((N, 0))
while q:
    now, cnt = q.popleft()
    if now == M:
        print(cnt+1)
        flag = 1
        break
    if now*2 <= max_q:
        q.append((now*2, cnt+1))
    now = now*10+1
    if now <= max_q:
        q.append((now, cnt+1))
if flag == 0:
    print(-1)
