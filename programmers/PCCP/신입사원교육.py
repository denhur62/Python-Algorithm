from heapq import heappop, heappush, heapify
def solution(ability, number):
    answer = []
    heapify(ability)
    while number:
        first = heappop(ability)
        second = heappop(ability)
        heappush(ability, first+second)
        heappush(ability, first+second)
        number-=1
    
    return sum(ability)

ability = [1, 2, 3, 4]
number = 3
print(solution(ability,number))


