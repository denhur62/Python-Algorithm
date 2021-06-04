import sys


s = sys.stdin.readline().rstrip()
explore = sys.stdin.readline().rstrip()
lene = len(explore)
lastc = explore[-1]
stack = []
for i in s:
    stack.append(i)
    if i == lastc:
        rever = "".join(stack[-lene:])
        if rever == explore:
            del stack[-lene:]

if stack:
    print(''.join(stack))
else:
    print("FRULA")
