import enum


def solution(s):
    answer = []
    list_s = s.split()
    
    for i in list_s:
        temp = ""
        for index, element in enumerate(i):
            if index % 2==0 : 
                temp += element.upper()
            else:
                temp += element.lower()
        answer.append(temp)
    answer = " ".join(answer)
    return answer


print(solution("t tT"))