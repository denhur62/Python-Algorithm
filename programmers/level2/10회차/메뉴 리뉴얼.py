from itertools import combinations
from collections import defaultdict
def solution(orders, course):
    orders=["".join(sorted(list(x))) for x in orders]
    answer=[]
    for i in course:
        temp=defaultdict(int)
        for j in orders:
            for k in combinations(j,i):
                temp["".join(k)]+=1
        if temp:
            temp= sorted(temp.items(), key=lambda x:x[1], reverse=True)
            max_temp=temp[0][1]
            for i in temp:
                if i[1]>=2 and max_temp==i[1]:
                    answer.append(i[0])
                else:
                    break
        
    return sorted(answer)

orders= ["XYZ", "XWY", "WXA"]
course=[2,3,4]

print(solution(orders,course))


# def solution(orders, course):
#     result = []

#     for course_size in course:
#         order_combinations = []
#         for order in orders:
#             order_combinations += itertools.combinations(sorted(order), course_size)

#         most_ordered = collections.Counter(order_combinations).most_common()
#         result += [ k for k, v in most_ordered if v > 1 and v == most_ordered[0][1] ]

#     return [ ''.join(v) for v in sorted(result) ]