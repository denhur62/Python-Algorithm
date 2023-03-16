from collections import deque
def solution(maps):
    map_y = len(maps)
    map_x = len(maps[0])
    flag =False
    for idx,i in enumerate(maps):
        for jdx,j in enumerate(i):
            if j=='S':
                s_y,s_x,l_c = bfs(maps,map_y,map_x,idx,jdx,'L')
                if s_y == -1:
                    return -1
                flag = True
                break
        if flag:
            break
    answer = bfs(maps,map_y,map_x,s_y,s_x,'E')
    if l_c !=-1 and answer[0]!= -1:
        return l_c+answer[0]
    else:
        return -1

def bfs(maps, map_y, map_x, start_y,start_x, target):
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    cnt=0
    visit = [[0 for _ in range(map_x)] for _ in range(map_y)] 
    queue=deque()
    queue.append((start_y,start_x,cnt))
    while queue:
        s_y , s_x, c = queue.popleft()
        if maps[s_y][s_x] == target:
            if target== 'L':
                return (s_y,s_x, c)
            else :
                return (c,-1,-1)
        for i in range(4):
            nx = dx[i] + s_x
            ny = dy[i] + s_y
            if 0<= ny<map_y and 0<= nx<map_x \
            and (maps[ny][nx] == 'O' or maps[ny][nx] == 'L' or maps[ny][nx] =='E' or maps[ny][nx] == 'S') \
            and (visit[ny][nx] == 0 or visit[ny][nx] > c+1) :
                visit[ny][nx] = c+1                
                queue.append((ny,nx,c+1))
    return (-1,-1,-1)
        

print(solution(["SOOOL","XXXXO","OOOOO","OXXXX","OOOOE"]))