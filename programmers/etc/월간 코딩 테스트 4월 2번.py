from collections import deque

def transform(s):
    temp=s.popleft()
    s.append(temp)
    return s
def correctstack(s):
    stack=deque()
    for i in s:
        if not stack:
            stack.append(i)
        else:
            if (stack[-1]=='[' and i==']') or (stack[-1]=='{' and i=='}') or (stack[-1]=='(' and i==')'):
                stack.pop()
            else:
                stack.append(i)
    if not stack:
        return True
    else:
        return False

def solution(s):
    lens=len(s)
    s=deque(s)
    cnt=0
    for i in range(lens):
        if correctstack(s):
            cnt+=1
        s=transform(s)
    return cnt


print(solution("[)(]"))