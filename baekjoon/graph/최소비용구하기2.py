from collections import deque,defaultdict
import sys
from heapq import heappush, heappop
N=int(input())
M=int(input())
dic=defaultdict(dict)
A,B,C=[],[],[]
for i in range(M):
    a,b,c=map(int,sys.stdin.readline().split())
    dic[a][b]=c
    A.append(a)
    B.append(b)
    C.append(c)
for i in range(M):
    a,b,c=A.pop(),B.pop(),C.pop()
    if dic[a][b]>c:
        dic[a][b]=c

start,end= map(int,input().split())

distance={node: [float("inf"),0] for node in range(1,N+1)}
distance[start]=[0,start]
queue=[]
heappush(queue,[0,start])
while queue:
    dis,node = heappop(queue)
    if distance[node][0] < dis:
        continue
    for next_node,next_dis in dic[node].items():
        final_dis=dis+next_dis
        if final_dis < distance[next_node][0]:
            distance[next_node]=[final_dis,node]
            heappush(queue,(final_dis,next_node))
temp=[]
temp.append(end)
while distance[end][1]!=start:
    temp.append(distance[end][1])
    end=distance[end][1]

print(distance[start][0])
print(len(temp))
print(*temp[::-1])

