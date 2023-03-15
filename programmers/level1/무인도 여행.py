def solution(maps):
    x_len = len(maps[0])
    y_len = len(maps)
    visit = [[0] * x_len for i in range(y_len)]
    answer=[]
    for idx, i in enumerate(maps):
        for jdx, j in enumerate(i):
            if j!='X' and visit[idx][jdx] == 0:
                cnt, visit = bfs(idx,jdx,visit,maps,x_len,y_len)
                answer.append(cnt)
    if answer:
        answer.sort()
    else :
        answer = [-1]    
    return answer

def bfs(j,i,visit,maps,x_len,y_len):
    cnt=0
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    node = [[j,i]]
    visit[j][i] = 1
    while node:
        pos = node.pop()
        cnt+=int(maps[pos[0]][pos[1]])
        for i in range(0,4):
            nx = pos[1] + dx[i]
            ny = pos[0] + dy[i]
            if 0<=nx<x_len and 0<=ny<y_len and visit[ny][nx] ==0 and maps[ny][nx] != 'X':
                visit[ny][nx]=1
                node.append([ny,nx])

                
    return cnt, visit

maps=["XXX","XXX","XXX"]
print(solution(maps))

