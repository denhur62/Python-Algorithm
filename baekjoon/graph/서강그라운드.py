from collections import deque,defaultdict
import sys

N,M,R=map(int,input().split())
item=[0]+list(map(int,sys.stdin.readline().split()))
dic=defaultdict(lambda :dict())
for i in range(R):
    a,b,c=map(int,sys.stdin.readline().split())
    dic[a][b]=c
    dic[b][a]=c
def dijstra(start):
    distances={node:float('inf') for node in range(1,N+1)}
    distances[start]=0
    queue=deque()
    queue.append([0,start])
    while queue:
        distance,node = queue.popleft()
        if distance > distances[node]:
            continue
        for new_node,new_distance in dic[node].items():
            dis=new_distance+distance
            if dis < distances[new_node]:
                queue.append([dis,new_node])
                distances[new_node]=dis
    return distances

answer=0
for i in range(1,N+1):
    dis=dijstra(i)
    temp=0
    for key,value in dis.items():
        if value<=M:
            temp+=item[key]
    if answer <temp:
        answer=temp
print(answer)
