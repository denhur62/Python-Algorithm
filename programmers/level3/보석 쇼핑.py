from collections import defaultdict
def solution(gems):
    lsg=len(set(gems))
    dic=defaultdict(int)
    start, end = 0, 0
    short=len(gems)
    answer=[]
    while end<len(gems):
        dic[gems[end]]+=1
        if len(dic)== lsg:
            while start<=end and len(dic)==lsg:
                print(dic,start,end)
                if dic[gems[start]]>1:
                    dic[gems[start]]-=1
                    start+=1
                else:
                    del dic[gems[start]]
                    start+=1
                if short > end -start:
                    short=end-start
                    answer=[start,end+1]
        end+=1
    return answer


gems=["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]
print(solution(gems))