from collections import defaultdict
def solution(input_string):
    sequence = input_string[0]
    dic = defaultdict(int)
    answer = set()
    for i in input_string:
        if dic[i]==0:
            dic[i]+=1
        elif dic[i]!=0 and sequence !=i:
            answer.add(i)
        sequence = i
    answer= list(answer)
    answer.sort()
    answer = "".join(answer)
    
    return answer if answer else "N"