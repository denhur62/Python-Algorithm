from collections import defaultdict
from itertools import combinations
import bisect
def solution(info, query):
    answer = []
    group=defaultdict(list)
    for i in info:
        temp=i.split()
        score=int(temp.pop())
        for j in range(0,5):
            for k in combinations(temp,j):
                group["".join(k)].append(score)
    for i in group.keys():
        group[i].sort()
    for i in query:
        temp=i.split(" ")
        search=int(temp.pop())
        temp = [ x for x in temp if x!='and' and x!='-']
        temp = "".join(temp)
        lo=bisect.bisect_left(group[temp],search)
        answer.append(len(group[temp])-lo)
    return answer


info=["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
query=["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]
print(solution(info,query))