import sys


while True:
    N = sys.stdin.readline().rstrip()
    if N == '0':
        break
    if len(N) % 2 == 0:
        length = len(N)//2
        left = N[:length]
        right = N[length:]
    else:
        length = len(N)//2
        left = N[:length+1]
        right = N[length:]
    if left == right[::-1]:
        print("yes")
    else:
        print('no')
