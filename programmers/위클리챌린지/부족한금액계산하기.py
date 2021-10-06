def solution(weights, head2head):
    answer = []
    lh=len(head2head)
    temp=[]
    for i in range(lh):
        win=0
        for j in range(lh):
            if weights[i] < weights[j]: win+=1
        temp.append([[head2head[i]/lh,win,weights[i],i]])
    print(temp)

    return answer