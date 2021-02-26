from collections import Counter
N = int(input())
arr = []
for i in range(N):
    arr.append(int(input()))
arr.sort()
print(round(sum(arr)/N))
print(arr[N//2])
bin = Counter(arr)
max_count = max(bin.values())
arr2 = []
for i in bin:
    if bin[i] == max_count:
        arr2.append(i)
if len(arr2) == 1:
    print(arr2[0])
else:
    print(arr2[1])
print(arr[-1]-arr[0])
