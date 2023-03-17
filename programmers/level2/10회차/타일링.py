import sys
sys.setrecursionlimit(30000)
def solution(n):
    arr = [0] * 60000
    a=1
    b=2
    for i in range(3,n+1):
        c=a+b
        a,b =b,c 
    return c % 1000000007

print(solution(4))