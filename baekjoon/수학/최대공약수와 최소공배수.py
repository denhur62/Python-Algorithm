from math import gcd

N, M = map(int, input().split())
g = gcd(N, M)
print(g)
print(g*(N//g)*(M//g))
