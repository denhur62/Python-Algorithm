from collections import defaultdict
def dfs(wires,visited,start):
    stack=[start]
    visited[start]=1
    cnt=1
    temp=[]
    while stack:
        idx=stack.pop()
        for i in wires[idx]:
            if visited[i]==0:
                visited[i]=1
                stack.append(i)
                cnt+=1
                temp.append(i)
    return cnt


def solution(n, wires):
    temp=[]
    answer=[]
    for i in range(n):
        temp2=wires[:i]+wires[i+1:]
        temp.append(temp2)
    for i in temp:
        wires=defaultdict(lambda:[])
        for a,b in i:
            wires[a].append(b)
            wires[b].append(a)
        visited=[0]*(n+1)
        flag=True
        a, b =0 ,0
        for j in range(1,n+1):
            if visited[j]==0:
                if flag:
                    a =dfs(wires,visited,j)
                    flag=False
                else:
                    b= dfs(wires,visited,j)
        answer.append(abs(a-b))
    return min(answer)



n=7
wires=[[1,2],[2,7],[3,7],[3,4],[4,5],[6,7]]
print(solution(n,wires))