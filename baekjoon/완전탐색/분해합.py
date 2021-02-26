

n = int(input())
flag = 0
for i in range(n):
    a = list(str(i))
    b = list(map(int, a))
    if sum(b)+i == n:
        print(int("".join(a)))
        flag = 1
        break
if flag == 0:
    print(0)
