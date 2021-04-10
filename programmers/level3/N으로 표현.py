def solution(N, number):
    answer = -1
    first = lambda x,y:int(str(x)*y)
    oper= lambda x,y:[x+y,x-y,x*y,x//y if y!=0 else 0]
    DP=[0]
    for i in range(1,9):
        temp=set([first(N,i)])
        for j in range(1,i):
            k=i-j
            for a in DP[j]:
                for b in DP[k]:
                    temp.update(oper(a,b))

        if number in temp:
            return i
        DP.append(temp)
        print(DP)
    return answer

N, number= 5, 12
print(solution(N,number))