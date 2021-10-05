import sys
from collections import deque
N=int(input())
arr=[]
for i in range(N):
    arr.append(list(map(int,sys.stdin.readline().split())))
max_rain=max(sum(arr,[]))
min_rain=min(sum(arr,[]))

def bfs(i,j,arr,visited,N):
    nx=[-1,1,0,0]
    ny=[0,0,-1,1]
    queue=deque()
    queue.append((i,j))
    while queue:
        (y,x)=queue.popleft()
        for i in range(4):
            dy=ny[i]+y
            dx=nx[i]+x
            if 0<=dy<N and 0<=dx<N and visited[dy][dx]==0 and arr[dy][dx]==0:
                visited[dy][dx]=1
                queue.append((dy,dx))



answer=[]
for i in range(min_rain,max_rain):
    arr2=arr[:]
    temp=[]
    for j in arr2:
        temp2=[]
        for k in j:
            if k >i:
                temp2+=[0]
            else:
                temp2+=[1]
        temp.append(temp2)
    visited=[[0] * N for _ in range(N)]
    cnt=0 
    for jj in range(N):
        for kk in range(N):
            if temp[jj][kk]==0 and visited[jj][kk]==0:
                visited[jj][kk]=1
                bfs(jj,kk,temp,visited,N)
                cnt+=1
    answer.append(cnt)
if answer:
    print(max(answer))
else:
    print(1)


