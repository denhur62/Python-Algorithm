M,N = map(int,input().split())

arr=[True]*(M+1)
cnt=0
for i in range(2,M+1):
    if arr[i]==True:
        cnt+=1
        if cnt==N:
            print(i)
            break
        for j in range(i+i,M+1,i):
            if arr[j]==True:
                cnt+=1
                arr[j]=False
            if cnt==N:
                print(j)
                break