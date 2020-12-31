import sys

N = int(input())

for i in range(N):
    stack = []
    for j in sys.stdin.readline().strip():
        if stack and stack[-1] == '(' and j == ')':
            stack.pop()
        else:
            stack += j
    print("YES") if not stack else print("NO")
