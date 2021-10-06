from collections import deque 
def solution(enter, leave): 
    answer = [0] * (len(enter)+1) 
    enter, leave,room = deque(enter), deque(leave),set() 
    temp = [] 
    while leave: 
        cur=leave.popleft()
        while enter and cur not in room: 
            room.add(enter.popleft()) 
        room.remove(cur)
        for s in room: 
            answer[cur] +=1 
            answer[s] +=1 
    return answer[1:]

enter=[3,2,1]
leave=[1,3,2]
print(solution(enter,leave))