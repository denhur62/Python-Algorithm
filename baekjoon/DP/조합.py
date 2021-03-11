

a, b = map(int, input().split())
if b == 1:
    print(a)
else:
    dp = [0]*101
    dp[1] = 1
    dp[2] = 2
    for i in range(3, 101):
        dp[i] = dp[i-1]*i
    print(dp[a]//(dp[a-b]*dp[b]))
