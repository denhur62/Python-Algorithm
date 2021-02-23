
n = int(input())
result = 0
count_5 = n//5
while True:
    result = n-count_5*5
    if result % 3 != 0 and count_5 == 0:
        print(-1)
        break
    elif result % 3 != 0 and count_5 != 0:
        count_5 -= 1
    else:
        print(count_5 + result//3)
        break
