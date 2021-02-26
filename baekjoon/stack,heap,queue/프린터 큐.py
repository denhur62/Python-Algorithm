import sys
N = int(input())

for i in range(N):
    M, index = map(int, sys.stdin.readline().split())
    arr = list(map(int, sys.stdin.readline().split()))
    order = 0
    max_arr = sorted(arr, reverse=True)
    j = 0
    k = 0
    while True:
        if arr[j] == max_arr[k]:
            order += 1
            if j == index:
                print(order)
                break
            k += 1
        j = (j+1) % M
