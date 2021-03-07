import sys
N = int(input())


def bfs():
    stack = [0]
    visited = [True]*(M+2)
    visited[0] = False
    while stack:
        s = stack.pop()
        for i in range(M+2):
            if visited[i] == True and answer[s][i] <= 1000 and s != i:
                print(answer[s][i], s, i)
                visited[i] = False
                stack.append(i)
    if visited[M+1] == False:
        print('happy')
    else:
        print('sad')


for _ in range(N):
    M = int(input())
    arr = []
    for i in range(M+2):
        temp = list(map(int, sys.stdin.readline().split()))
        arr.append(temp)
    answer = [[0]*(M+2) for _ in range(M+2)]
    for i in range(M+2):
        for j in range(i+1, M+2):
            dis = abs(arr[i][0]-arr[j][0])+abs(arr[i][1]-arr[j][1])
            answer[i][j] = dis
            answer[j][i] = dis
    print(answer)
    bfs()
