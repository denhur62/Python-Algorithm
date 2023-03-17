from collections import Counter

def solution(k, tangerine):
    dic = Counter(tangerine)

    real_dict = dict(sorted(dic.items(),key= lambda x: -x[1]))
    answer = 0
    for i in real_dict.keys():
        k-=real_dict[i]
        answer+=1
        if k<=0:
            return answer
print(solution(2, [1, 1, 1, 1, 2, 2, 2, 3]))