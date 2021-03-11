import sys
N = int(input())


for _ in range(N):
    len_arr = int(input())
    upper_arr = list(map(int, sys.stdin.readline().split()))
    lower_arr = list(map(int, sys.stdin.readline().split()))
    DP = [[0]*len_arr for _ in range(3)]
    DP[0][0] = upper_arr[0]
    DP[1][0] = lower_arr[0]
    DP[2][0] = 0
    for i in range(1, len_arr):
        DP[0][i] = upper_arr[i]+max(DP[1][i-1], DP[2][i-1])
        DP[1][i] = lower_arr[i]+max(DP[0][i-1], DP[2][i-1])
        DP[2][i] = 0+max(DP[0][i-1], DP[1][i-1])
    print(max(DP[0][-1], DP[1][-1], DP[2][-1]))
