from collections import defaultdict
import math
def solution(weights):
    wl = [0] * 4001
    answer=0
    for i in weights:
        wl[i] +=1
        wl[int(i*1.5)] +=1
        wl[i*2] +=1
        wl[int(i*2/3)] +=1
        wl[int(i*4/3)] +=1 
        wl[int(i*0.5)] +=1
        wl[int(i*3/4)] +=1

    for i in weights:
        print(i, wl[i])
        if wl[i]:
            answer+=1


    return answer

print(solution([100,180,360,100,270,540]))

