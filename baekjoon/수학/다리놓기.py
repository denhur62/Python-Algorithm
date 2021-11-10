N=int(input())
for i in range(N):
    a,b=map(int,input().split())
    answer=1
    div=1
    for j in range(b-a+1,b+1):
        answer*=j
    for j in range(1,a+1):
        div*=j
    print(answer//div)
