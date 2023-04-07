from collections import deque
def solution(plans):
    
    answer = []
    plan_array = []
    idx =0
    for subject, s, e in plans:
        temp = s.split(":")
        start = int(temp[0])*60 + int(temp[1])
        plan_array.append([start,int(e),subject])
        idx+=1
    plans = deque(sorted(plan_array, key= lambda x:x[0]))
    wait_stack = []
    while plans:
        start, duration, subject = plans.popleft()
        if plans:
            if start+duration <= plans[0][0]:
                answer.append(subject)
                remain_time = plans[0][0] - start - duration
                flag = True
                while flag and wait_stack:
                    start,duration,subject = wait_stack.pop()
                    if remain_time >= duration:
                        remain_time -= duration
                        answer.append(subject)
                    else:
                        duration -= remain_time
                        wait_stack.append([start,duration,subject])
                        flag = False
            else:
                temp = start + duration - plans[0][0]
                wait_stack.append([start,temp,subject])
        else:
            answer.append(subject)
    for i in wait_stack[::-1]:
        answer.append(i[2])
    return answer

a = [["1", "00:00", "30"], ["2", "00:10", "10"], ["3", "00:30", "10"], ["4", "00:50", "10"]]
print(solution(a))