def solution(stones, k):
    start=0
    end=200000000
    mid=end//2
    answer=0
    while start<=end:
        mid=(start+end)//2
        stone=[i-mid for i in stones]
        print(stone, mid)
        i, flag=0 , False
        while i<len(stone) and not flag :
            if stone[i]<=0:
                cnt=0
                while i<len(stone) and stone[i]<=0 :
                    cnt+=1
                    i+=1
                if cnt>=k:
                    flag=True
            else:
                i+=1
        if flag:
            answer=mid
            end=mid-1
        else:
            start=mid+1
    return answer            


stones=[2, 4, 5, 3, 2, 1, 4, 2, 5, 1]
k=3
print(solution(stones,k))