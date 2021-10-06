def solution(weights, head2head):
    answer = []
    lh=len(head2head)
    temp=[]
    for i in range(lh):
        win=0
        for j in range(lh):
            if weights[i] < weights[j] and head2head[i][j]=="W": win+=1
            N=head2head[i].count("N")
        if N==lh:
            temp.append([0.0,win,weights[i]])
        else:
            temp.append([head2head[i].count("W")/(lh-head2head[i].count("N")),win,weights[i]])
    dic={a+1:b for a,b in enumerate(temp) }
    dic=sorted(dic.items(),key = lambda x:x[1],reverse=True)

    answer=[x[0] for x in dic]
    return answer