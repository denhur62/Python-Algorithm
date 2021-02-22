from collections import defaultdict
from itertools import combinations


def combi(n, m):
    answer = 1
    for i in range(n-m+1, n+1):
        answer *= i
    for i in range(1, m+1):
        answer /= i
    return answer


def solution(clothes):
    answer = len(clothes)
    dic = defaultdict(lambda: [])
    for i in clothes:
        dic[i[1]].append(i[0])
    for i in range(2, len(dic.keys())):
        c = combi

    print(dic)
    return answer


clothes = [["yellow_hat", "headgear"], [
    "blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]
print(solution(clothes))
