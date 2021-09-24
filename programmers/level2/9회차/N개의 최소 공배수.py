
def uc(a,b):
    
    la, lb=a,b
    if(b>a) : a,b = b,a

    while(a!=b):
        if(a>b) : a-=b
        else    : b-=a
    la, lb = la//a , lb//a
    return a*la*lb
    

def solution(arr):
    while len(arr)>=2:
        print(arr)
        a=arr.pop()
        b=arr.pop()
        arr.append(uc(a,b))
    return arr[0]