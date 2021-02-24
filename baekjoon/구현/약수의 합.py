import sys

N = int(sys.stdin.readline().strip())
count = 0
for i in range(1, N+1):
    count += int(N/i)*i
print(count)
