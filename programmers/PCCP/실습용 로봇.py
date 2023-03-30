def solution(command):
    cur_direct = '+y'
    answer =[0,0]
    for i in command:
        print(answer)
        if i == 'R':
            if cur_direct == '+y':
                cur_direct = '+x'
            elif cur_direct == '-y':
                cur_direct = '-x'
            elif cur_direct == '+x':
                cur_direct = '-y'
            else:
                cur_direct = '+y'
        if i == 'L':
            if cur_direct == '+y':
                cur_direct = '-x'
            elif cur_direct == '-y':
                cur_direct = '+x'
            elif cur_direct == '+x':
                cur_direct = '+y'
            else:
                cur_direct = '-y'
        if i == 'G':
            if cur_direct == '+y':
                answer[0]+=1
            if cur_direct == '-y':
                answer[0]-=1
            if cur_direct == '+x':
                answer[1]+=1
            if cur_direct == '-x':
                answer[1]-=1
        if i == 'B':
            if cur_direct == '+y':
                answer[0]-=1
            if cur_direct == '-y':
                answer[0]+=1
            if cur_direct == '+x':
                answer[1]-=1
            if cur_direct == '-x':
                answer[1]+=1
    return [answer[1],answer[0]]

print(solution("GRGRGRB"))