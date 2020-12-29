import sys

s = sys.stdin.readline().strip()
count1 = 0
count2 = 0
for i in s:
    if (i == 'p' or i == 'P'):
        count1 += 1
    if (i == 'y' or i == 'Y'):
        count2 += 1
print("true") if count1 == count2 else print("false")
