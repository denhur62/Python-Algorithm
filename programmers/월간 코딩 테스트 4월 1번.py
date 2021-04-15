

def solution(absolutes, signs):
    answer = 0
    for i in range(len(signs)):
        if signs[i]=="true":
            answer+=absolutes[i]
        else:
            answer+=(-1)*absolutes[i]
    return answer


absolutes=[4,7,12]
signs=["true","false","true"]
print(solution(absolutes,signs))
