import sys
from collections import defaultdict

N = int(input())


def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union(parent, a, b):
    if a not in parent:
        parent[a] = a
        number[a] = 1
    if b not in parent:
        parent[b] = b
        number[b] = 1

    parent_a = find_parent(parent, a)
    parent_b = find_parent(parent, b)

    if parent_a != parent_b:
        parent[parent_a] = parent_b
        number[parent_b] += number[parent_a]
    print(number[parent_b])


for i in range(N):
    M = int(input())
    parent = {}
    number = defaultdict(str)
    for j in range(M):
        a, b = sys.stdin.readline().split()
        union(parent, a, b)
