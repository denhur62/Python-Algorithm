
arr = [(0, 0)]*41
arr[0] = (1, 0)
arr[1] = (0, 1)
for i in range(2, 41):
    arr[i] = (arr[i-1][0]+arr[i-2][0], arr[i-1][1]+arr[i-2][1])

N = int(input())

for i in range(N):
    M = int(input())
    print(*arr[M])
