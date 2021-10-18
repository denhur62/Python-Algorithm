from collections import deque

nx=[1,-1,0,0]
ny=[0,0,1,-1]
def check(rectangle,room,y,x):
    cnt=0
    flag=0
    for minx,miny,maxx,maxy in rectangle:
        if minx<x<maxx and miny<y<maxy:
            cnt+=1
    if cnt==0:
        return True
    else:
        return False
def check2(temp,y,x):
    for i in temp:
        for y1,x1 in i:
            if y==y1 and x==x1:
                return True
    return False
def subrectangle(room,y,x):
    answer=[]
    for i in room:
        for y1,x1 in i:
            if y==y1 and x==x1:
                answer.append(i)
    return answer

def bfs(rectangle,startY,startX,itemY,itemX,room):
    queue=deque()
    temp=subrectangle(room,startY,startX)
    queue.append((startY,startX,0,temp))
    visited=[[0]*51 for _ in range(51)]
    visited[startY][startX]=1
    while queue:
        y,x,cnt,te =queue.popleft()
        print(y,x)
        if y==itemY and x==itemX:
            return cnt
        for i in range(4):
            dy=y+ny[i]
            dx=x+nx[i]
            if (1<=dy<=50 and 1<=dx<=50 and visited[dy][dx]==0
                and check(rectangle,room,dy,dx) and check2(te,dy,dx)):
                temp= subrectangle(room,dy,dx)
                visited[dy][dx]=1
                queue.append((dy,dx,cnt+1,temp))


def solution(rectangle, characterX, characterY, itemX, itemY):
    temp=[]
    for x1,y1,x2,y2 in rectangle:
        room=set()
        for y in range(y1,y2+1):
            room.add((y,x1))
            room.add((y,x2))
        for x in range(x1,x2+1):
            room.add((y1,x))
            room.add((y2,x))
        temp.append(room)
    answer= bfs(rectangle,characterY,characterX,itemY,itemX,temp)
    return answer


rectangle=[[2,2,5,5],[1,3,6,4],[3,1,4,6]]
characterX=1
characterY=4
itemX=6
itemY=3

print(solution(rectangle,characterX,characterY,itemX,itemY))