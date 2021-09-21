
def solution(number, k):
    answer=[]
    for i in number:
        print(answer,k)
        if not answer or answer[-1] > i or k==0:
            answer.append(i)
        else:
            while k>0 and answer and answer[-1] < i:
                answer.pop()
                k-=1
            answer.append(i)
    if k!=0:
        return "".join(answer[:len(number)-k])
    else:
        return "".join(answer)

print(solution("4177252841",4))