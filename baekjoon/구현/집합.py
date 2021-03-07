import sys

N = int(input())
s = set()
for _ in range(N):
    a = sys.stdin.readline().rstrip().split()
    if len(a) == 2:
        a[1] = int(a[1])
        if a[0] == 'add':
            s.add(a[1])
        elif a[0] == 'remove':
            if a[1] in s:
                s.remove(a[1])
        elif a[0] == 'check':
            if a[1] in s:
                print(1)
            else:
                print(0)
        elif a[0] == 'toggle':
            if a[1] in s:
                s.remove(a[1])
            else:
                s.add(a[1])
    else:
        if a[0] == 'all':
            s = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11,
                 12, 13, 14, 15, 16, 17, 18, 19, 20}
        elif a[0] == 'empty':
            s = set()
