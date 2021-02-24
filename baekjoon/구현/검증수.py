import sys

N = list(map(int, sys.stdin.readline().split()))

N = list(map(lambda x: x**2, N))
print(sum(N) % 10)
