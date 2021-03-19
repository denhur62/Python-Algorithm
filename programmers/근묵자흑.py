import sys

N, K = map(int, sys.stdin.readline().split())

arr = list(map(int, sys.stdin.readline().split()))

if N > K:
    if (N-K) % (K-1) != 0:
        print(1+(N-K)//(K-1)+1)
    else:
        print(1+(N-K)//(K-1))
else:
    print(1)
