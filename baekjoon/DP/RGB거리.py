import sys
N = int(input())

arr = []
for i in range(N):
    arr.append(list(map(int, sys.stdin.readline().split())))


def RGB():
    for i in range(N):
        if i == 0:
            dp[0][0] = arr[0][0]
            dp[0][1] = arr[0][1]
            dp[0][2] = arr[0][2]
        else:
            dp[i][0] = arr[i][0]+min(dp[i-1][2], dp[i-1][1])
            dp[i][1] = arr[i][1]+min(dp[i-1][0], dp[i-1][2])
            dp[i][2] = arr[i][2]+min(dp[i-1][1], dp[i-1][0])
    return min(dp[N-1][0], dp[N-1][1], dp[N-1][2])


answer = []
dp = [[0]*3 for _ in range(N)]
print(RGB())
