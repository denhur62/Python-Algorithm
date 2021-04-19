import sys
sys.setrecursionlimit(10 ** 9)


def solution(start, end):
    if start > end:
        return

    middle = end+1
    for i in range(start+1, end+1):
        if tree[start] < tree[i]:
            middle = i
            break

    solution(start+1, middle-1)
    solution(middle, end)
    print(tree[start])


tree = []
count = 0
while count <= 10000:

    try:
        temp = int(input())
    except:
        break
    tree.append(temp)
    count += 1

solution(0, len(tree)-1)
