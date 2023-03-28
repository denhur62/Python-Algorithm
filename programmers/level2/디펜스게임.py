from heapq import heappop, heappush
def solution(n, k, enemy):
    answer = 0
    heap =[]
    kill_enemy =0
    for i in enemy:
        heappush(heap,-i)
        kill_enemy+=i
        if kill_enemy > n:
            if k == 0:
                break
            kill_enemy += heappop(heap)
            k-=1
            
        answer+=1

    return answer


n= 2
k= 4
enemy = 	[3, 3, 3, 3]
print(solution(n,k,	enemy))


