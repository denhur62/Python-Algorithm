import sys
from collections import defaultdict, deque

total = int(input())


def solution(f, arr):
    arr = deque(arr)
    temp = 'error'
    status = True
    for i in f:
        if i == 'R':
            status = not status
        else:
            if not arr or arr[0] == '':
                return temp
            else:
                if status:
                    arr.popleft()
                else:
                    arr.pop()
    if not status:
        arr.reverse()
    temp = ",".join(list(arr))
    return '['+temp+']'


for i in range(total):
    function = input()
    N = int(input())
    arr = list(input()[1:-1].split(','))
    print(solution(function, arr))
