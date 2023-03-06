def solution(t, p):
    p_len = len(p)
    temp =[]
    answer=0
    for i in range(len(t)-p_len+1):
        temp.append(t[i:i+p_len])
    
    for i in temp:
        if p >= i:
            answer+=1
    return answer

t= "3141592"
p= 	"271"	
print(solution(t,p))