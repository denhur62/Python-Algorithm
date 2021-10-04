import sys
sys.setrecursionlimit(10000000)
def recur(number,room):
    if number not in room:
        room[number]=number+1
        return number
    key=recur(room[number],room)
    room[key]=key+1
    return key

def solution(k, room_number):
    room=dict()
    answer=[]
    for i in room_number:
        j= recur(i,room)
        answer.append(j)
    return answer