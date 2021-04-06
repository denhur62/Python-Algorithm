from collections import deque
import sys
N,M=map(int,sys.stdin.readline().split())
ladder=[]
for i in range(N):
    NN,MM=map(int,input().split())
    ladder.append((NN,MM))
snake=[]
for j in range(M):
    NN,MM=map(int,input().split())
    snake.append((NN,MM))
def check(queue,s,c,visited):
    for i1,i2 in ladder:
        if s==i1 and visited[i2]==False:
            visited[i2]=True
            queue.append((i2,c))
            return False
    for j1,j2 in snake:
        if s==j1 and visited[j2]==False:
            visited[j2]=True
            queue.append((j2,c))
            return False
    return True
def dfs(start):
    queue=deque()
    answer=float('inf')
    queue.append((start,0))
    visited=[False]*101
    while queue:
        s,c= queue.popleft()
        if s==100:
            if answer>c:
                answer=c
        elif s>100:
            continue
        else:
            if check(queue,s,c,visited):
                for i in range(1,7):
                    if s+i<=100 and visited[s+i]==False:
                        visited[s+i]=True
                        queue.append((s+i,c+1))
    return answer
        
        
        



print(dfs(1))
