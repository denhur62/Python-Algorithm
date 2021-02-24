import sys

N = int(input())
M = list(map(int, sys.stdin.readline().split()))

d = [0]*(N+1)
d[0] = M[0]
d[1] = max(d[0], M[1])
for i in range(2, N):
    d[i] = max(d[i-1], d[i-2]+M[i])

print(d[N-1])
