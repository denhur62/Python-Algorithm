import sys

N, M = map(int, input().split())
see = set()
listen = set()
for _ in range(N):
    see.add(input())

for _ in range(M):
    listen.add(input())

answer = see & listen
answer = sorted(list(answer))
print(len(answer))
for i in answer:
    print(i)
