def solution(sizes):
    left,right=[],[]
    for a,b in sizes:
        if a>b:
            left.append(a)
            right.append(b)
        else:
            left.append(b)
            right.append(a)
    return max(left)*max(right)

s=[[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]]
print(solution(s))