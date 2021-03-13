import sys

sys.setrecursionlimit(10**9)

N = int(input())
arr = []
for i in range(N):
    arr.append(sys.stdin.readline().rstrip())


def quard(i, j, n):
    nn = n//2
    hap = 0
    check = arr[i][j]
    flag = 0
    for y in range(i, i+n):
        for x in range(j, j+n):
            if arr[y][x] != check:
                flag = 1
                break
    if flag == 1:
        return '('+quard(i, j, nn)+quard(i, j+nn, nn) + \
            quard(i+nn, j, nn)+quard(i+nn, j+nn, nn)+')'
    else:
        return check


answer = quard(0, 0, N)
print(quard(0, 0, N))
