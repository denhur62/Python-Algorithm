

inputString = input()
j = 0
cnt = 0
answer = 0
flag = 0
stack = []
for i in inputString:
    print(i)
    if i == '(' or i == '[' or i == '{' or i == '<':
        stack.append(i)
    if (i == ')' and stack[-1] == '(') or (i == ']' and stack[-1] == '[') or (i == '}' and stack[-1] == '{') or (i == '>' and stack[-1] == '<'):
        cnt += 1
        stack.pop()
    elif (i == ')' and stack[-1] != '(') or (i == ']' and stack[-1] != '[') or (i == '}' and stack[-1] != '{') or (i == '>' and stack[-1] != '<'):
        print(-1*j)
        flag = 1
        break
    j += 1
if flag == 0:
    if not stack:
        print(cnt)
    else:
        print(-1*len(inputString)+1)
