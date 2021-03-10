import sys


sample = sys.stdin.readline().rstrip()
find = sys.stdin.readline().rstrip()
table = [0]*len(find)
result = []
count = 0


def maketable(find):
    j = 0
    for i in range(1, len(find)):
        while j > 0 and find[i] != find[j]:
            j = table[j-1]
        if find[i] == find[j]:
            j += 1
            table[i] = j


def solution(find, count):
    j = 0
    for i in range(0, len(sample)):
        while j > 0 and sample[i] != find[j]:
            j = table[j-1]
        if sample[i] == find[j]:
            if j == len(find)-1:
                result.append(i-len(find)+2)
                count += 1
                j = table[j]
            else:
                j += 1
    return count


maketable(find)
count = solution(find, count)
print(count)
for i in result:
    print(i)
