def solution(citations):
    for i in range(max(citations), 0, -1):
        if len(list(filter(lambda x: x <= i, citations))) <= i and len(list(filter(lambda x: x >= i, citations))) >= i:
            return i
    return 0
