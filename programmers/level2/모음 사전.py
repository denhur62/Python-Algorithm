from collections import deque


def solution(word):
    temp = ['A', 'E', 'I', 'O', 'U']
    cnt = 0
    queue = deque(temp)
    while queue:
        cha = queue.popleft()
        cnt += 1
        if cha == word:
            return cnt
        else:
            if len(cha) != 5:
                for i in temp[::-1]:
                    re = cha+i
                    queue.appendleft(re)


print(solution("EIO"))
