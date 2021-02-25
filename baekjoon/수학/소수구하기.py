

N, M = map(int, input().split())

arr = [True]*(M+1)
arr[1] = False
for i in range(2, int(M**0.5)+1):
    if arr[i] == True:
        for j in range(i+i, M+1, i):
            arr[j] = False
for i in range(N, M+1):
    if arr[i] == True:
        print(i)
