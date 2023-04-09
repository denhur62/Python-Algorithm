def solution(left, right):
    answer = 0
    for i in range(left,right+1):
        temp = measure_cnt(i)
        if temp%2==0:
            answer+=i
        else:
            answer-=i

    return answer

def measure_cnt(n):
    cnt=0
    for i in range(1,n+1):
        if n%i==0:
            cnt+=1
    return cnt