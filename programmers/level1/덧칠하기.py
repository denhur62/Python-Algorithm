from collections import deque
def solution(n, m, section):
    queue = deque(section)
    answer = 0
    while queue:
        print(queue)
        first= queue[0]
        while queue and first+m >queue[0]:
            queue.popleft()
        answer+=1
    return answer


print(solution(8,4,[2,3,6]))