# 음수 간선은 두개 넣으 면 안됨
import sys
from collections import defaultdict
N = int(input())


def bell():
    distance = {node: 10001 for node in range(1, a+1)}
    for i in range(1, a+1):
        for j in range(1, a+1):
            for k in matrix[j]:
                end, weight = k
                if distance[end] > weight+distance[j]:
                    distance[end] = weight+distance[j]
                    if i == a:
                        return False
    return True


for _ in range(N):
    a, b, c = map(int, sys.stdin.readline().split())
    matrix = defaultdict(lambda: [])
    for _ in range(b):
        x, y, z = map(int, sys.stdin.readline().split())
        matrix[x].append((y, z))
        matrix[y].append((x, z))
    for _ in range(c):
        x, y, z = map(int, sys.stdin.readline().split())
        matrix[x].append((y, -z))
    if bell():
        print("NO")
    else:
        print("YES")
