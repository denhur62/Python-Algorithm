import sys
from collections import Counter
from itertools import combinations
N, M = map(int, sys.stdin.readline().split())

arr = []

for i in range(int(N)):
    temp = sys.stdin.readline().rstrip()
    arr.append(temp[4:-4])
if M-5 < 0:
    print(0)
    exit(0)

middle = []
learn = 'antic'
answer2 = ''
for i in arr:
    answer = ''
    for j in i:
        if j not in learn and j not in answer:
            answer += j
    middle.append(answer)
    answer2 += answer
temp = list(combinations(answer2, M-5))
max_count = 0
answer = 0
for i in temp:
    a = "".join(i)
    max_count = 0
    for j in middle:
        count = 0
        for k in j:
            if k in a:
                count += 1
        if count == len(j):
            max_count += 1

    if answer < max_count:
        answer = max_count

print(arr)
