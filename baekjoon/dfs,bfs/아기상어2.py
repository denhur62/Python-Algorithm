from collections import deque
M,N=map(int,input().split())
temp=[]
for i in range(M):
    temp.append(list(map(int,input().split())))

ny=[1,1,1,0,0,-1,-1,-1]
nx=[-1,0,1,-1,1,-1,0,1]
def bfs(i,j):
    queue=deque()
    queue.append((i,j,0))
    visited=[[0]*N for _ in range(M)]
    visited[i][j]=1
    while queue:
        y,x,cnt = queue.popleft()
        if temp[y][x]==1:
            return cnt
        for i in range(8):
            dy=y+ny[i]
            dx=x+nx[i]
            if 0<=dy<M and 0<=dx<N and visited[dy][dx]==0:
                visited[dy][dx]=1
                queue.append((dy,dx,cnt+1))
answer=[]
for i in range(M):
    for j in range(N):
        if temp[i][j]==0:
            answer.append(bfs(i,j))
print(max(answer))

