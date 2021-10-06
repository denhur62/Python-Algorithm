def solution(scores):
    answer = []
    ls=len(scores)
    for i in range(ls):
        temp=[j[i] for j in scores]
        max_t=max(temp)
        min_t=min(temp)
        if (((temp.count(max_t)==1 and max_t==scores[i][i])
            or (temp.count(min_t)==1 and min_t==scores[i][i]))
            and (scores[i][i]== min_t or scores[i][i]==max_t)):
            answer.append((sum(temp)-scores[i][i])/(ls-1))
        else:
            answer.append(sum(temp)/ls)
    temp=[]
    for i in answer:
        if i>=90:
            temp.append("A")
        elif 80<= i<90:
            temp.append("B")
        elif 70<= i <80:
            temp.append("C")
        elif 50<= i <70:
            temp.append("D")
        else:
            temp.append("F")