def solution(lottos, win_nums):
    order ={6:1,5:2,4:3,3:4,2:5,1:6,0:6}
    zero = lottos.count(0)
    lottos = [x for x in lottos if x!=0]
    win_nums = set(win_nums)
    cnt=0
    for i in lottos:
        if i in win_nums:
            cnt+=1
    return [order[cnt+zero],order[cnt]]