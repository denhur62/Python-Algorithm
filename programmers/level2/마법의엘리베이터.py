import sys
sys.setrecursionlimit(1500000)
def solution(storey):
    visit = [0]*(storey+1)
    floor = []
    i= 1
    while i<= 100_000_000:
        if i <= storey:
            floor.extend([i,-i])
        else:
            break
        i*=10
    bfs(storey, visit,storey,floor)
    return visit[0]

def bfs(start,visit,storey, floor):
    for i in floor:
        if i<0:
            if start+i>=0 and (visit[start+i] > visit[start]+1 or visit[start+i] == 0):
                visit[start+i] = visit[start]+1
                bfs(start+i,visit,storey,floor)
        else:
            if start+i < storey and (visit[start+i] > visit[start]+1 or visit[start+i] ==0):
                visit[start+i] = visit[start]+1
                bfs(start+i,visit,storey,floor)




print(solution(2))


