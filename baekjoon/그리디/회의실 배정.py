import sys

N = int(input())
arr = []
for i in range(N):
    b = list(map(int, sys.stdin.readline().split()))
    arr.append(b)
arr = sorted(arr, key=lambda x: (x[1], x[0]))
count = 0
end = 0
for i in arr:
    s, e = i
    if end <= s:
        count += 1
        end = e
print(count)
