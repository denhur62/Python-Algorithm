def solution(order):
    second = []
    answer = 0 
    s, e = order[0], len(order)
    stack=[]
    idx=0
    for i in range(1,e+1):
        stack.append(i)
        while stack and stack[-1] == order[idx]:
            stack.pop()
            answer+=1
            idx+=1
    return answer