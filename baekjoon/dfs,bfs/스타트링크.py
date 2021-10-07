import sys
from collections import deque
max_floor, start, goal,up,down=map(int,sys.stdin.readline().split())
visited=[0]*(max_floor+1)
queue=deque()
queue.append((start,0))
flag=True
while queue:
    cur,cnt=queue.popleft()
    if cur==goal:
        print(cnt)
        flag=False
        break
    if cur+up<=max_floor and visited[cur+up]==0:
        visited[cur+up]=1
        queue.append((cur+up,cnt+1))
    if cur-down>=1 and visited[cur-down]==0:
        visited[cur-down]=1
        queue.append((cur-down,cnt+1))
if flag:
    print("use the stairs")

