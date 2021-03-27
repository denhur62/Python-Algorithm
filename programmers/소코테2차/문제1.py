import sys

N,M=sys.stdin.readline().split()
N=int(N)
M=M.split(":")
M=int(M[0])*3600+int(M[1])*60+int(M[2])

def trans(temp):
    temp=temp.split(":")
    return int(temp[0])*60+int(temp[1])
arr=[]
for i in range(N):
    temp=sys.stdin.readline().rstrip()
    arr.append(trans(temp))
max_cnt,start=0,0
for i in range(0,len(arr)):
    cnt=0
    temp=0
    for j in range(i,len(arr)):
        temp+=arr[j]
        cnt+=1
        if temp>=M:
            break
        
    if max_cnt<cnt:
        max_cnt=cnt
        start=i
print(max_cnt,start+1)