def solution(scores):
    answer = []
    ls=len(scores)
    for i in range(ls):
        temp=[]
        cnt=0
        for j in range(ls):
            if j==i and len(set(scores[i]))==len(scores[i]) and max(scores[i])== scores[i][j]:
               cnt+=1
            else:
                temp.append(ls[i][j])
        answer.append(sum(temp)/(ls-cnt))
    print(answer)
    return answer
print(solution([1,2,3,4]))