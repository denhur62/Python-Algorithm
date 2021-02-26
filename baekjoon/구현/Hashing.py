
N = int(input())
temp = list(input())
temp = list(map(lambda x: ord(x)-96, temp))
cnt = 0
for i in range(N):
    cnt += temp[i]*31**i
print(cnt % 1234567891)
