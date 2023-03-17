from collections import deque
def solution(board):
    answer = -1
    for ydx,y in enumerate(board):
        for xdx,x in enumerate(y):
            if x == 'R':
                return bfs(board,ydx,xdx)
                


def bfs(board,start_y,start_x):
    board_y = len(board)
    board_x = len(board[0])
    visit = [[0 for _ in range(board_x)] for _ in range(board_y)] 
    queue = deque()
    queue.append((start_y,start_x))
    while queue:
        y, x = queue.popleft() 
        if board[y][x] =='G':
            return visit[y][x]
        top, bottom, left, right = 0, 0, 0, 0
        while 0<=bottom+y+1<board_y and board[bottom+y+1][x]!= 'D':
            bottom+=1
        while 0<=y-top-1<board_y and board[y-top-1][x]!= 'D':
            top+=1
        while 0<=x-left-1<board_x and board[y][x-left-1]!= 'D':
            left+=1
        while 0<=x+right+1<board_x and board[y][x+right+1]!= 'D':
            right+=1
        
        dx = [0,0,-left,right]
        dy = [-top,+bottom,0,0]
        for i in range(4):
            if dy[i]== 0 and dx[i] ==0:
                continue
            ny= y+dy[i]
            nx= x+dx[i]
            if visit[ny][nx]== 0 or visit[ny][nx] > visit[y][x]+1:
                visit[ny][nx] = visit[y][x] +1
                queue.append((ny,nx))
    return -1

    


print(solution(	[".D.R", "....", ".G..", "...D"]))