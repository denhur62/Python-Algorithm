import sys

while True:
    stack = []
    line = map(str, sys.stdin.readline().rstrip())
    for idx, each in enumerate(line):
        if each == '.' and idx == 0:
            sys.exit(0)
        else:
            if stack and stack[-1] == '[' and each == ']':
                stack.pop()
            elif stack and stack[-1] == '(' and each == ')':
                stack.pop()
            elif each == ')' or each == '(' or each == '[' or each == ']':
                stack += [each]
    if not stack:
        print("yes")
    else:
        print("no")
