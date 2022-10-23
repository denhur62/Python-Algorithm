import enum


def solution(strings, n):
    strings.sort()
    return sorted(strings, key= lambda x: x[n])


print(solution(["sun", "bed", "car"], 1))