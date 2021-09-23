from itertools import combinations


def solution(enter, leave):
    answer = [0]* (len(enter)+1)
    meet_list = []
    set_list = []
    for l in leave:
        meet_list = [x for x in set(enter[0:enter.index(l)+1])  if x not in set(leave[0:leave.index(l)])]
        if(len(meet_list) == 1): continue

        for n in combinations(meet_list,2):
            set_list.append(n)

    for n in set(set_list):
        answer[n[0]] +=1
        answer[n[1]] +=1

    return answer[1:]
    


enter = [1,4,2,3]
leave = [2,1,3,4]
print(solution(enter,leave))
