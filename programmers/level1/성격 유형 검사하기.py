from collections import defaultdict
def solution(survey, choices):
    dic = defaultdict(int)
    score = [0,3,2,1,0,1,2,3]
    for index,i in enumerate(survey):
        be, af = i[0], i[1]
        if 1<=choices[index]<=3:
            dic[be] += score[choices[index]]
        if 4<= choices[index] <=7:
            dic[af] += score[choices[index]]    
    answer = ''
    if dic['R'] >= dic['T']:
        answer+='R'
    else:
        answer+='T'
    if dic['C'] >= dic['F']:
        answer+='C'
    else:
        answer+='F'
    if dic['J'] >= dic['M']:
        answer+='J'
    else:
        answer+='M'
    if dic['A'] >= dic['N']:
        answer+='A'
    else:
        answer+='N'
    return answer

survey = ["TR", "RT", "TR"]
choices = 	[7, 1, 3]
print(solution(survey, choices))  