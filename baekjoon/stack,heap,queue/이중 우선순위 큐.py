import sys
from collections import deque, defaultdict
from bisect import bisect_left

N = int(input())


def sl(b):
    if not stack:
        stack.append(b)
    else:
        temp = bisect_left(stack, b)
        stack.insert(temp, b)


for _ in range(N):
    M = int(input())
    stack = deque()
    count = 0
    dic = defaultdict(int)
    for _ in range(M):
        a, b = sys.stdin.readline().split()
        b = int(b)
        if a == 'I':
            if dic[b] == 0:
                sl(b)
                dic[b] = 1
            else:
                dic[b] += 1
        else:
            if b == 1 and stack:
                if dic[stack[-1]] == 1:
                    dic[stack[-1]] -= 1
                    stack.pop()
                else:
                    dic[stack[-1]] -= 1
            elif b == -1 and stack:
                if dic[stack[0]] == 1:
                    dic[stack[0]] -= 1
                    stack.popleft()
                else:
                    dic[stack[0]] -= 1
    if stack:
        print(max(stack), min(stack))
    else:
        print("EMPTY")
