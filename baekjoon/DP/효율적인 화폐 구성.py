import sys

N, M = map(int, sys.stdin.readline().split())
coin = []
for i in range(N):
    coin.append(int(input()))
coin.sort()
d = [float('inf')]*10001
for i in coin:
    d[i] = 1
for i in range(coin[-1]+1, M+1):
    for j in coin:
        if d[i-j] != -1:
            d[i] = min(d[i-j]+1, d[i])

if d[M] == float('inf'):
    print(-1)
else:
    print(d[M])
