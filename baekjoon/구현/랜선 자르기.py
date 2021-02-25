import sys

N, M = map(int, sys.stdin.readline().split())
arr = []
for i in range(N):
    arr.append(int(sys.stdin.readline().rstrip()))

arr.sort()


def solution(arr):
    start = 1
    end = arr[-1]
    while start <= end:
        middle = (start+end)//2
        cnt = 0
        for i in arr:
            cnt += i//middle
        if cnt < M:
            end = middle-1
        else:
            start = middle+1
    return end


print(solution(arr))
