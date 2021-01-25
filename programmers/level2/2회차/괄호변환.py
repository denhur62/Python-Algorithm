
def solution(p):
    u = ''
    v = ''
    answer = ''
    empty = ''
    if iscorrect(p):
        return p
    else:
        u, v = separation(p)
        answer += u
    if iscorrect(u):
        u = solution(v)
        answer += u
        return answer
    else:
        empty += '('
        empty += solution(v)
        empty = empty+')'+rever(u)
    return empty

def rever(p):
    q = list(p)
    del q[0]
    del q[len(q)-1] #q[1:-1]
    for idx, val in enumerate(q):
        if(val == ')'):
            q[idx] = '('
        else:
            q[idx] = ')'
    p = "".join(q)
    return p


def separation(p):
    front = []
    back = []
    strfront = ''
    backfront = ''
    for idx, val in enumerate(p):
        front.append(val)
        if front.count('(') == front.count(')'):
            strfront = "".join(front)
            if(idx == len(p)-1):
                backfront = ""
            else:
                backfront = "".join(p[idx+1:])
            break
    return strfront, backfront


def isbalance(p):
    if p.count(')') == p.count('('):
        return True
    else:
        return False


def iscorrect(p):
    stack = []
    for i in p:
        if not stack:
            stack.append(i)
        elif stack[-1] == '(' and i == ')':
            stack.pop()
        else:
            stack.append(i)
    if not stack:
        return True
    else:
        return False


print(solution(p))
print('()(())()')
