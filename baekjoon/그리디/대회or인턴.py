import sys

N,M,K = map(int,sys.stdin.readline().split())

for i  in range(1,100):
    nn=N-(i*2)
    mm=M-i
    if nn<0 or mm<0 or nn+mm<K:
        print(i-1)
        break

    