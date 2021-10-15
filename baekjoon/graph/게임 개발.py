from collections import deque, defaultdict
import sys

M=int(input())
time=[0]
queue=deque()
key= defaultdict(lambda: [])
degree=[0 for i in range(M+1)]
DP=[0 for i in range(M+1)]
for i in range(M):
    temp=list(map(int,sys.stdin.readline().split()))
    time.append(temp[0])
    for j in temp[1:-1]:
        key[j].append(i+1)
        degree[i+1]+=1
for i in range(1,M+1):
    if degree[i]==0:
        queue.append(i)
        DP[i]=time[i]
while queue:
    start = queue.popleft()
    for i in key[start]:
        degree[i]-=1
        DP[i]=max(DP[i], time[i]+DP[start])
        if degree[i]==0:
            queue.append(i)
for i in DP[1:]:
    print(i)
