import sys

N,M=map(int,input().split())
temp=list(map(int,sys.stdin.readline().split()))
start, end=0,0
answer=0
aw=100000001
while True:
    if answer>=M:
        aw=min(aw,end-start)
        answer-=temp[start]
        start+=1
        
    elif end==N:
        break
    else:
        answer+=temp[end]
        end+=1
if aw==100000001:
    print(0)
else:
    print(aw)