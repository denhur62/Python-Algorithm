import sys
from heapq import heappush, heappop
from collections import defaultdict
a , b= map(int,sys.stdin.readline().split())
dic=defaultdict(lambda :defaultdict())
for i in range(b):
    q ,w ,e=map(int,sys.stdin.readline().split())
    dic[q][w]=e
    dic[w][q]=e
start, end=map(int,sys.stdin.readline().split())

def dijstra(start,end):
    queue=[]
    distance={node: float("inf") for node in range(1,a+1)}
    distance[start]=0
    heappush(queue,[0,start])
    while queue:
        dis,node=heappop(queue)
        if distance[node] < dis:
            continue
        for next_node , new_dis in dic[node].items():
            nd=new_dis+dis
            if distance[next_node] > nd:
                distance[next_node]=nd
                heappush(queue,[nd,next_node])
    return distance[end]
dis1=dijstra(1,start)+dijstra(start,end)+dijstra(end,a)
dis2=dijstra(1,end)+dijstra(end,start)+dijstra(start,a)

if dis1==float("inf") and dis2==float("inf"):
    print(-1)
else:
    print(min(dis1,dis2)) 



