import sys

N = int(input())
M = int(input())
io = input()
cnt = 0
answer = 0
i = 1
while i < M-1:
    if io[i-1] == 'I' and io[i] == 'O' and io[i+1] == 'I':
        cnt += 1
        if cnt == N:
            cnt -= 1
            answer += 1
        i += 1
    else:
        cnt = 0
    i += 1
print(answer)
