import sys
sys.setrecursionlimit(30000)

N=int(sys.stdin.readline())


max_arr=[0]*3
min_arr=[0]*3
max_temp=[0]*3
min_temp=[0]*3
for i in range(N):
    a,b,c= map(int,sys.stdin.readline().split())
    for j in range(3):
        if j==0:
            max_temp[j]=max(max_arr[j],max_arr[j+1])+a
            min_temp[j]=min(min_arr[j],min_arr[j+1])+a
        elif j==1:
            max_temp[j]=max(max_arr[j-1],max_arr[j],max_arr[j+1])+b
            min_temp[j]=min(min_arr[j-1],min_arr[j],min_arr[j+1])+b
        else:
            max_temp[j]=max(max_arr[j],max_arr[j-1])+c
            min_temp[j]=min(min_arr[j],min_arr[j-1])+c
    for k in range(3):
        max_arr[k]=max_temp[k]
        min_arr[k]=min_temp[k]
print(max(max_arr),min(min_arr))
