answer=0
def dfs(d,visited,cur,cnt,len_d,mf):
    global answer
    if cur<mf or sum(visited)==len_d:
        answer=max(answer,cnt)
        return 
    for i in range(len_d):
        if visited[i]==0 and cur>= d[i][0]:
            cur-=d[i][1]
            visited[i]=1
            dfs(d,visited,cur,cnt+1,len_d,mf)
            cur+=d[i][1]
            visited[i]=0
    



def solution(k, dungeons):
    global answer
    len_d=len(dungeons)
    min_fatigue=min([i[0] for i in dungeons])
    visited=[0]*len_d
    for i in range(len_d):
        if dungeons[i][0]<=k:
            visited[i]=1
            dfs(dungeons,visited,k-dungeons[i][1],1,len_d,min_fatigue)
            visited[i]=0
            
    return answer
d=[[80,20],[50,40],[30,10]]	
k=80
print(solution(k,d))