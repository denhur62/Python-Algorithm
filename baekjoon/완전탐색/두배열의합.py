import sys
from collections import defaultdict

input = sys.stdin.readline

T = int(input())
N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))

dicA=defaultdict(int)
answer=0
for i in range(N):
    for j in range(i,N):
        dicA[sum(A[i:j+1])]+=1
for i in range(M):
    for j in range(i,M):
        answer+=dicA[T-sum(B[i:j+1])]
print(answer)