from collections import deque
def solution(queue1, queue2):
    q1_sum = sum(queue1)
    q2_sum = sum(queue2)
    equal_sum= (q1_sum+ q2_sum)//2
    answer = 0
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    cnt=0
    while (queue1 and queue2) and cnt<=6000000:
        if q1_sum == q2_sum and q1_sum ==equal_sum:
            return answer
        elif q1_sum >q2_sum:
            temp = queue1.popleft()
            queue2.append(temp)
            q2_sum+= temp
            q1_sum-= temp
            answer+=1
            cnt+=1
        else :
            temp = queue2.popleft()
            queue1.append(temp)
            q2_sum-=temp
            q1_sum+=temp
            answer+=1
            cnt+=1
    return -1