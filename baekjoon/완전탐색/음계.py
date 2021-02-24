import sys
a = [1, 2, 3, 4, 5, 6, 7, 8]
b = [8, 7, 6, 5, 4, 3, 2, 1]

N = list(map(int, sys.stdin.readline().split()))
if a == N:
    print("ascending")
elif b == N:
    print("descending")
else:
    print("mixed")
