import sys
Q, E, W,S,N = map(int,sys.stdin.readline().split())
percent=[E,W,S,N]
e=(0,1)
w=(0,-1)
n=(1,0)
s=(-1,0)
def dfs(y,x,cnt,te):
    global answer
    if cnt==Q:
        answer+=te
        return 
    for l,i in enumerate([e,w,n,s]):
        dy=y+i[0]
        dx=x+i[1]
        if visited[dy][dx]==0 and 0<=dy<(2*Q)+1 and 0<=dx<(2*Q)+1:
            visited[dy][dx]=1
            dfs(dy,dx,cnt+1,te*percent[l]/100)
            visited[dy][dx]=0

answer=0
visited=[[0] * (2 * Q + 1) for _ in range(2 * Q + 1)]
visited[Q][Q]=1
dfs(Q,Q,0,1)
print(answer)
