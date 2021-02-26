import sys

N = int(input())
arr = []
for i in range(N):
    member_age, member_name = map(str, input().split())
    member_age = int(member_age)
    arr.append((member_age, member_name))

arr = sorted(arr, key=lambda x: x[0])
for i in arr:
    print(*i)
