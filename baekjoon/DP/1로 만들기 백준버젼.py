
N = int(input())
x = [float('inf')]*1000001
x[1] = 0
x[2] = 1
x[3] = 1

for i in range(4, N+1):
    if i % 3 == 0:
        x[i] = min(x[i], x[i//3]+1)
    if i % 2 == 0:
        x[i] = min(x[i], x[i//2]+1)
    x[i] = min(x[i], x[i-1]+1)
print(x[N])
