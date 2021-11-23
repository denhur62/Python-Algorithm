N=int(input())

for i in range(int(N**0.5)+1,0,-1):
    if i*i>=N:
        print(i)
        break