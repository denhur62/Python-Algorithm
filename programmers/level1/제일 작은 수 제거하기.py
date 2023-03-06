def solution(arr): 
    del arr[arr.index(min(arr))]
    if len(arr) == 0 :
        return [-1]
    else:
        return arr


arr = [4,3,2,1,1]
print(solution(arr))