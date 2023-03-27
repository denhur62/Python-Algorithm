from itertools import permutations
def solution(n, k):
    list_n = [i for i in range(1,n+1)]
    temp = permutations(list_n,n)
    temp2 = sorted(temp,key=lambda x:x)
    return list(temp2)[k-1]



print(solution(3,5))