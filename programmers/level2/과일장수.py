def solution(k, m, score):
    score.sort(reverse=True)
    
    answer = 0
    for i in range(0,len(score),m):
        if len(score[i:i+m]) == m:
            answer += score[i+m-1] * m
    return answer


print(solution(4,3,	[4, 1, 2, 2, 4, 4, 4, 4, 1, 2, 4, 2]))