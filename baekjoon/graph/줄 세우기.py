from collections import deque, defaultdict
M,N=map(int,input().split())

queue=deque()
key= defaultdict(lambda: [])
degree=[0 for i in range(M+1)]
answer=[]

for i in range(N):
    a ,b =map(int,input().split())
    key[a].append(b)
    degree[b]+=1
for i in range(1,M+1):
    if degree[i]==0:
        queue.append(i)
while queue:
    start=queue.popleft()
    answer.append(start)
    for i in key[start]:
        degree[i]-=1
        if degree[i]==0:
            queue.append(i)
print(*answer)




