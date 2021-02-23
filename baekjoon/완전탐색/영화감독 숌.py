
c = 665
N = int(input())
cnt = 0
while True:
    c += 1
    if '666' in str(c):
        cnt += 1
    if cnt == N:
        break
print(c)
