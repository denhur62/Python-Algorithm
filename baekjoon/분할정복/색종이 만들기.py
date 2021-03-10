import sys

N = int(input())
arr = [[]*N for _ in range(N)]
for i in range(N):
    arr[i] += list(map(int, sys.stdin.readline().split()))


def quad(x, y, n):
    col, row = 0, 0
    if n == 1:
        if arr[y][x] == 1:
            return (0, 1)
        else:
            return (1, 0)
    else:
        check = arr[y][x]
        flag = 0
        for i in range(n):
            for j in range(n):
                if arr[y+i][x+j] != check:
                    flag = 1
                    break
        if flag == 1:
            _c, _r = quad(x, y, n//2)
            col += _c
            row += _r
            _c, _r = quad(x+n//2, y, n//2)
            col += _c
            row += _r
            _c, _r = quad(x, y+n//2, n//2)
            col += _c
            row += _r
            _c, _r = quad(x+n//2, y+n//2, n//2)
            col += _c
            row += _r
            return (col, row)
        else:
            if check == 1:
                return (0, 1)
            else:
                return (1, 0)


t = quad(0, 0, N)
print(t[0])
print(t[1])
