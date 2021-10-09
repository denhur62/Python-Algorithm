
X , Y = map(int,input().split())
win=Y*100//X
start=X
end=1000000000
answer=[]
while start<=end:
    mid=(start+end)//2
    temp= (Y+mid-X)*100//mid
    if win<temp:
        answer.append(mid-X)
        end=mid-1
    else:
        start=mid+1
if not answer:
    print(-1)
else:
    print(min(answer))