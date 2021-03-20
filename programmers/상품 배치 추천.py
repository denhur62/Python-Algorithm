import sys

N = int(input())
arr = []
answer = [0]*(N+1)
for i in range(N):
    arr.append(list(map(int, sys.stdin.readline().rstrip())))

for k in range(1, N):
    for i in range(N-k+1):
        for j in range(N-k+1):
            flag = True
            for ii in range(i, i+k):
                for jj in range(j, j+k):
                    if arr[ii][jj] != 1:
                        flag = False
                        break
            if flag:
                answer[k] += 1
print("total:", sum(answer))
for i in range(1, N):
    if answer[i] != 0:
        print("size["+str(i)+"]: "+str(answer[i]))
