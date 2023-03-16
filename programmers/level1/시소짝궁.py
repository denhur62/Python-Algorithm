from collections import defaultdict
import math
def solution(weights):
    wl = [0] * 4001
    answer=0
    for i in weights:
        wl[i] +=1
        wl[i*2] +=1 
        wl[i*3] +=1
        wl[i*4] +=1
    for idx,i in enumerate(wl):
        if i!=0:
            print(idx,i)
    for i in weights:
        if wl[i] >=2:
            answer += math.comb(wl[i],2)

    return answer

print(solution([100,180,360,100,270]))