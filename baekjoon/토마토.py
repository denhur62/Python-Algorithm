import sys
import collections

a=list(map(int,sys.stdin.readline().split()))
arr=[list(map(int,sys.stdin.readline().split()))for i in range(a[1])]
queue=collections.deque([])
visited=[[0 for i in range(a[0])] for j in range(a[1])]
cell_count=0
answer_count=0
flag=0
for idx,ival in enumerate(arr):
    for jdx,jval in enumerate(ival):
        if(jval==1):
            queue.append((idx,jdx))
            visited[idx][jdx]=1
            cell_count+=1
        if(jval==-1):
            cell_count+=1
queue.append((-2,-2))
while queue:
    x,y=queue.popleft()
    if 0< x + 1 < a[1] and visited[x+1][y] == 0 and arr[x+1][y] == 0:
        visited[x+1][y] = visited[x][y] + 1
        cell_count+=1
        queue.append((x+1, y))
        flag=1
    if 0 <= x - 1  and visited[x-1][y] == 0 and arr[x-1][y] == 0:
        visited[x-1][y] = visited[x][y] + 1
        cell_count+=1
        queue.append((x-1, y))
        flag=1
    if 0< y + 1 < a[0] and visited[x][y + 1] == 0 and arr[x][y + 1] == 0:
        visited[x][y + 1] = visited[x][y] + 1
        cell_count+=1
        queue.append((x, y + 1))
        flag=1
    if 0 <= y - 1 and visited[x][y - 1] == 0 and arr[x][y - 1] == 0:
        visited[x][y - 1] = visited[x][y] + 1
        cell_count+=1
        queue.append((x, y - 1))
        flag=1
    if x==-2 and flag==1:
        answer_count+=1
        queue.append((-2,-2))
        flag=0
if cell_count==a[0]*a[1]:
    print(answer_count)
else:
    print(-1)




