

def solution(gems):
    N = len(set(gems))
    last = len(gems)
    start, end = 0, 0
    while end < last:
        if len(set(gems[start:end])) == N:
            break
        end += 1
    while start < end and len(set(gems[start:end])) == N:
        start += 1

    return [start, end]


gems = ["AA", "AB", "AC", "AA", "AC"]
print(solution(gems))
