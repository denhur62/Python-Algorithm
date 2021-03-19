import sys
N = int(input())

for i in range(N):
    x, y = map(int, sys.stdin.readline().split())
    cnt = 0
    while True:
        if x >= 5 and y >= 7:
            mod_x = x//5
            mod_y = y//7
            temp = min(mod_x, mod_y)
            cnt += temp
            x -= 5*temp
            y -= 7*temp
        elif x >= 12-y and y < 7:
            temp = 1+(x+y-12)//12
            cnt += temp
            break
        else:
            break
    print(cnt)
