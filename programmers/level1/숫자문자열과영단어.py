def solution(s):
    dic={"zero":0,"one":1,"two":2,"three":3,"four":4,
        "five":5,"six":6,"seven":7,"eight":8,"nine":9}
    answer=[]
    i=0
    while i<len(s):
        temp=[]
        if s[i].isalpha():
            while i<len(s) and s[i].isalpha() :
                temp.append(s[i])
                if "".join(temp) in dic.keys():
                    answer.append(dic["".join(temp)])
                    temp=[]
                i+=1
        else:
            answer.append(s[i])
            i+=1
    answer=list(map(str,answer))
    return int("".join(answer))

a="one4seveneight"
print(solution(a))