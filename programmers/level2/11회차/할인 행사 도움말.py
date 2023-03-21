from collections import Counter
def solution(want, number, discount):
    want_dic =dict()
    for i in range(len(number)):
        want_dic[want[i]] = number[i]
    answer=0
    for i in range(len(discount)):
        discount_dic = dict(Counter(discount[i:i+10]))
        flag= True
        for i in want_dic.keys():
            if discount_dic.get(i) == None:
                flag = False
                break
            elif want_dic[i]> discount_dic[i]:
                flag = False
                break
        if flag:
            answer+=1
    return answer

want = ["banana"]
number =[2]
discount = ["q","banana","banana","banana"]
print(solution(want,number,discount))
