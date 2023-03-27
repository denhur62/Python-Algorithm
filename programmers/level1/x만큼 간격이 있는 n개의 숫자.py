


def solution(x, n):
    answer = []
    for i in range(1,n+1):
        answer.append(x*i)
    return answer


print(solution([1,1,3,3,0,1,1]))