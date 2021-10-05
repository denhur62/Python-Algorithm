import sys
N=int(input())

def dfs(dic,start,visited):
    stack=[dic[start]]
    while stack:
        x=stack.pop()
        if visited[x]==0:
            visited[x]=1
            stack.append(dic[x])
        else:
            break
        

for i in range(N):
    M=int(input())
    arr=list(map(int,sys.stdin.readline().split()))
    temp=list(zip(enumerate(arr)))
    temp=sum(temp,())
    temp={a+1:b for a,b in temp}
    visited=[0]*(M+1)
    answer=0
    for i in arr:
        if visited[i]==0:
            visited[i]=1
            dfs(temp,i,visited)
            answer+=1
    print(answer)