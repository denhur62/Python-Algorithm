import sys
from itertools import permutations

N = int(input())
arr = []
for i in range(N):
    arr.append(list(map(int, sys.stdin.readline().split())))
answer = float('inf')


def check_zero(k):
    count = 0
    for j in range(N):
        if arr[k[j]][k[j+1]] == 0:
            return -1
        else:
            count += arr[k[j]][k[j+1]]
    return count


for i in permutations(range(N), N):
    k = i+(i[0],)
    count = check_zero(k)
    if count != -1:
        answer = min(count, answer)
print(answer)
