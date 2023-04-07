from collections import deque, defaultdict
def solution(sequence, k):
    dic = defaultdict()
    queue = deque()
    s_len = len(sequence)
    i=0
    answer= 0
    s,e, ss = 0,0, 0 
    while i<s_len:
        ss+= sequence[i]
        queue.append(sequence[i])
        e= i
        i+=1
        while ss >= k:
            if ss == k:
                if len(queue) not in dic.keys():
                    dic[len(queue)]  = [s,e]
                    
                break
            else:
                temp = queue.popleft()
                ss -= temp
                s+=1
            print(i, ss, queue,s,e)
    print(dic)
    dic = sorted(dic.items())
    answer = dic[0][1]
    return answer

sequence = [2, 2, 2, 2, 2]
k = 6
print(solution(sequence,k))