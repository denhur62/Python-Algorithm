def solution(keymap, targets):
    dic = dict()
    for i in keymap:
        for idx, j in enumerate(i):
            if dic.get(j) == None :
                dic[j]=idx+1
            elif dic[j] > idx:
                dic[j]=idx+1
    answer=[]
    print(dic)
    for i in targets:
        key=0
        for j in i:
            if dic.get(j) == None:
                key=-1
                break                
            else :
                key+=dic[j]
        answer.append(key)
    return answer


keymap=["AGZ", "BSSS"]
targets=["ASA","BGZ"]
print(solution(keymap,targets))
#1358