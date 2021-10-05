a,b= map(int,input().split())
room=set([a])
temp=[a]
while True:
    a=list(map(int,list(str(a))))
    a=sum(list(map(lambda x:x**b,a)))
    if a not in room:
        room.add(a)
        temp.append(a)
    else:
        idx=temp.index(a)
        print(idx)
        break