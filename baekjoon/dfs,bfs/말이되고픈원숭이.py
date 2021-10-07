import sys
from collections import deque
N=int(input())
a,b=map(int,input().split())
temp=[]
for i in range(b):
    temp.append(list(map(int,sys.stdin.readline().split())))
queue=deque()
queue.append((0,0,0,N))

nx=[1,-1,0,0]
ny=[0,0,1,-1]
hx=[2,2,1,1,-1,-1,-2,-2]
hy=[1,-1,2,-2,2,-2,1,-1]

visited=[[[0]*(N+1) for _ in range(a)] for _ in range(b)]
visited[0][0][N]=1
flag=True
while queue:
    y,x,cnt,k=queue.popleft()
    if (y,x)==(b-1,a-1):
        print(cnt)
        flag=False
        break
    for i in range(4):
        dx=x+nx[i]
        dy=y+ny[i]
        if 0<=dy<b and 0<=dx<a and temp[dy][dx]==0 and visited[dy][dx][k]==0:
            visited[dy][dx][k]=1
            queue.append((dy,dx,cnt+1,k))
    if k>0:
        for i in range(8):
            dx=x+hx[i]
            dy=y+hy[i]
            if 0<=dy<b and 0<=dx<a and temp[dy][dx]==0 and visited[dy][dx][k-1]==0:
                visited[dy][dx][k-1]=1
                queue.append((dy,dx,cnt+1,k-1))
if flag:
    print(-1)
