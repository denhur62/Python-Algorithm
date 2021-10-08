import sys
from collections import deque

N=int(input())

def minor(n):
    m=int(n**0.5)
    temp=[True]*n
    for i in range(2,m+1):
        if temp[i]==True:
            for j in range(i+i,n,i):
                temp[j]=False
    return temp

minor_list=minor(10000)
for i in range(N):
    a,b=map(int,input().split())
    a=list(str(a))
    queue=deque()
    queue.append((a,0))
    visited=[0]*10000
    flag=True
    while queue:
        start,cnt=queue.popleft()
        if int("".join(start))==b:
            print(cnt)
            flag=False
            break
        for j in range(4):
            for k in map(str,range(10)):
                if j==0 and k=='0':
                    continue
                num=start[:j]+[k]+start[j+1:]
                NUM=int("".join(num))
                if minor_list[NUM] and visited[NUM]==0:
                    visited[NUM]=1
                    queue.append((num,cnt+1))
    if flag:
        print("Impossible")



    