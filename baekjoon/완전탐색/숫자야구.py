import sys
from itertools import permutations
N=int(input())
temp = list(range(1,10))
temp2=[]
for i in permutations(temp,3):
    temp2.append(str(i[0])+str(i[1])+str(i[2]))

def getsb(number,temp):
    st=0
    b=0
    for i in range(3):
        if number[i]==temp[i]:
            st+=1
        else:
            if number[i] in set(temp):
                b+=1
    return st,b


for i in range(N):
    number,s,b =map(int,sys.stdin.readline().split())
    number=str(number)
    temp3=[]
    for j in temp2:
        st,ball=getsb(number,j)
        if s==st and b==ball:
            temp3.append(j)
    temp2=temp3
print(len(temp2))