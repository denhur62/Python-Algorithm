import sys

N = int(input())

stack = []

K = list(map(int, sys.stdin.read().split()))

for i in K:
    if i == 0:
        stack.pop()
    else:
        stack.append(i)

print(sum(stack))
