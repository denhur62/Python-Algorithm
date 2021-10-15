from collections import deque, defaultdict
import sys

K= int(input())
for k in range(K):
    M,N=map(int,input().split())
    time=list(map(int,sys.stdin.readline().split()))
    queue=deque()
    key= defaultdict(lambda: [])
    degree=[0 for i in range(M+1)]
    DP=[0 for i in range(M+1)]
    for i in range(N):
        a ,b =map(int,sys.stdin.readline().split())
        key[a].append(b)
        degree[b]+=1

    target=int(input())
    for i in range(1,M+1):
        if degree[i]==0:
            queue.append(i)
            DP[i]=time[i-1]

    while queue:
        start = queue.popleft()
        for i in key[start]:
            degree[i]-=1
            DP[i]=max(DP[i], time[i-1]+DP[start])
            if degree[i]==0:
                queue.append(i)
    print(DP[target])

