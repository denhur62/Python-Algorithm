
from itertools import combinations_with_replacement
from collections import Counter, defaultdict

def solution(n, info):
    info_dic = defaultdict(int)
    answer=[]
    max_score = 0
    score = [10,9,8,7,6,5,4,3,2,1,0]
    for idx,i in enumerate(info):
        info_dic[score[idx]]=i

    for i in combinations_with_replacement(range(11),n):
        temp =[0]*11
        e = Counter(i)
        apochi_score=0
        lion_score=0
        for jdx in range(10,-1,-1):
            if info_dic[jdx] >= e[jdx] and info_dic[jdx]!=0:
                apochi_score+=jdx
            if info_dic[jdx] < e[jdx]:
                lion_score+= jdx
        if apochi_score < lion_score:
            gap = lion_score - apochi_score
            for (k,v) in e.items():
                temp[score[k]]=v
            if answer:
                if max_score == gap:
                    for k in range(10,-1,-1):
                        if temp[k] > answer[k] :
                            
                            answer = temp[:]
                            break
                        if temp[k] < answer[k]:
                            break
                if max_score < gap:
                    answer= temp[:]
                    max_score = gap
            else:
                answer = temp[:]
                max_score = gap
            
    return answer if answer else [-1]



print(solution(10,	[0,0,0,0,0,0,0,0,3,4,3]))
