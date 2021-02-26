from collections import deque
import sys
n = int(input())

queue = deque()
for i in range(n):
    m = sys.stdin.readline().split()
    if len(m) == 1:
        if m[0] == 'front':
            if not queue:
                print(-1)
            else:
                print(queue[0])
        if m[0] == 'back':
            if not queue:
                print(-1)
            else:
                print(queue[-1])
        if m[0] == 'size':
            print(len(queue))
        if m[0] == 'empty':
            if not queue:
                print(1)
            else:
                print(0)
        if m[0] == 'pop_back':
            if not queue:
                print(-1)
            else:
                print(queue[-1])
                queue.pop()
        if m[0] == 'pop_front':
            if not queue:
                print(-1)
            else:
                print(queue[0])
                queue.popleft()
    else:
        if m[0] == 'push_back':
            queue.append(m[1])
        if m[0] == 'push_front':
            queue.appendleft(m[1])
