N=int(input())

def gcd(a,b):
    while b:
        a,b = b,a%b
    return a

for i in range(N):
    a,b= map(int,input().split())
    print(a*b//gcd(a,b))