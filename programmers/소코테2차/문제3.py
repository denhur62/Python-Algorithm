from heapdict import heapdict
import sys
from collections import defaultdict

N=int(input())
dic=defaultdict(lambda:{})
for i in range(N):
    a,b,c=sys.stdin.readline().split()
    c=int(c)
    dic[a][b]=c
    dic[b][a]=c
    if i==0:
        start=a
def prim(start):
    keys,pi,answer=heapdict(),dict(),0
    for i in dic.keys():
        keys[i]=float('inf')
        pi[i]=None
    keys[start],pi[start]=0,start

    while keys:
        now_node,now_key=keys.popitem()
        answer+=now_key
        for next_node, weight in dic[now_node].items():
            if next_node in keys and weight<keys[next_node]:
                keys[next_node]=weight
                pi[next_node]=now_node
    return answer

print(prim(start))
