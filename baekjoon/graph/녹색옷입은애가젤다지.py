import sys
from heapq import heappush, heappop
cnt=1
dx=[0,0,-1,1]
dy=[1,-1,0,0]
while True:
    N=int(input())
    if N==0:
        break
    temp=[]
    for i in range(N):
        temp.append(list(map(int,sys.stdin.readline().split())))
    distance=[[float('inf')]*N for _ in range(N)]
    queue=[]
    distance[0][0]=temp[0][0]
    heappush(queue,[temp[0][0],0,0])
    while queue:
        dis,y,x=heappop(queue)
        if y==N-1 and x==N-1:
            print("Problem {}:".format(cnt),distance[y][x])
        if distance[y][x] < dis:
            continue
        for i in range(4):
            ny=y+dy[i]
            nx=x+dx[i]
            if 0<=ny<N and 0<=nx<N:
                new_dis=dis+temp[ny][nx]
                if new_dis < distance[ny][nx]:
                    distance[ny][nx]=new_dis
                    heappush(queue,[new_dis,ny,nx])
    cnt+=1



