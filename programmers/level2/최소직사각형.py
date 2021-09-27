def recur(ls,i,a,left,right):
    if ls==i:
        return max(left)*max(right)
    else:
        answer = min(recur(ls,i+1,a,left+[a[0][i]],right+[a[1][i]]),
                    recur(ls,i+1,a,left+[a[1][i]],right+[a[0][i]]))
        return answer


def solution(sizes):
    a=list(map(list,zip(*sizes)))
    answer=recur(len(sizes),0,a,[],[])
    return answer

s=[[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]]
print(solution(s))