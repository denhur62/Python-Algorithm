from collections import defaultdict
def solution(table, languages, preference):
    dic=defaultdict(lambda : dict())
    for i in table:
        j=i.split()
        cnt=5
        for k in j[1:]:
            dic[j[0]][k]=cnt
            cnt-=1
    answer=defaultdict(int)
    for i,j in enumerate(languages):
        for k in dic.keys():
            if j in dic[k].keys():
                answer[k]+=dic[k][j]*preference[i]
    max_v=max(answer.values())
    answer=[k for k,v in answer.items() if max_v==v]
    answer.sort()
    return answer[0]

table=["SI JAVA JAVASCRIPT SQL PYTHON C#", "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++", "HARDWARE C C++ PYTHON JAVA JAVASCRIPT", "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP", "GAME C++ C# JAVASCRIPT C JAVA"]
languages=["JAVA", "JAVASCRIPT"]
preference=[7, 5]

print(solution(table,languages,preference))