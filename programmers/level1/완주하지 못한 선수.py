from collections import Counter
def solution(participant, completion):
    p=set(participant)
    c=set(completion)
    if p - p&c:
        return p-p&c
    else:
        a=Counter(participant)
        b=Counter(completion)
        for i in a.keys():
            if a[i]!=b[i]:
                return i



participant=["mislav", "stanko", "mislav", "ana"]
completion=["stanko", "ana", "mislav"]
print(solution(participant,completion))