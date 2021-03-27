import sys

N = int(input())

start = []
end = []


def split_string(string):
    result = string.split(':')
    return int(result[0])*60+int(result[1])


for i in range(N):
    temp = sys.stdin.readline().split()

    start.append(split_string(temp[0]))
    end.append(split_string(temp[2]))

start = max(start)
end = min(end)
if start > end:
    print(-1)
else:
    answer = str(start//60).rjust(2, '0')+':'+str(start % 60).rjust(2, '0') + \
        ' ~ ' + str(end//60).rjust(2, '0')+':'+str(end % 60).rjust(2, '0')
    print(answer)
