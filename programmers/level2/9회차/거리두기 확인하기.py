from collections import deque

def dfs(qy,qx,places):
    queue=deque()
    nx=[1,-1,0,0]
    ny=[0,0,1,-1]
    queue.append((qy,qx,2))
    flag=True
    while queue:
        y,x,z= queue.popleft()
        if flag==False:
            return False
        for i in range(4):
            dx=x+nx[i]
            dy=y+ny[i]
            if 0<=dx<5 and 0<=dy<5 and places[dy][dx]!='X' and z>0:
                if places[dy][dx]=='P' and (dx!=qx or dy!=qy):
                    print(1)
                    flag=False
                queue.append((dy,dx,z-1))
                
    return True
    
    
def solution(places):
    answer=[]
    for n in range(5):
        flag=True
        for i in range(5):
            for j in range(5):
                if places[n][i][j]=='P':
                    temp = dfs(i,j,places[n])
                    if temp == False:
                        flag=False
                        answer.append(0)
                if not flag:
                    break
            if not flag:
                break
        if flag:
            answer.append(1)
    return answer