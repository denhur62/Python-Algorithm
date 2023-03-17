import math
def solution(n, left, right):
    answer = []
    temp=[]
    k=left//n+1
    real_left=left//n
    
    for j in range(real_left,right//n+1): 
        arr=[k]*k+[i+1 for i in range(k,n)]
        k+=1
        temp.extend(arr)
        
    return temp[left%n:right-(left//n)*n+1]