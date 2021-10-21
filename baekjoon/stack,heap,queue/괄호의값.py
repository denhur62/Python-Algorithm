
S=input()
stack=[]
i=0
answer=0
while True:
    if i==len(S):
        break
    elif S[i]=="(" or S[i]=="[":
        stack.append(S[i])
        i+=1
    elif i<len(S) and stack and S[i]==")" and stack[-1]=="(":
        stack[-1]=2
        i+=1
    elif i<len(S) and stack and S[i]=="]" and stack[-1]=="[":
        stack[-1]=3
        i+=1
    else:
        te=0
        if S[i]==")":
            if not stack:
                print(0)
                exit(0)
            for k in range(len(stack)-1,-1,-1):
                if stack[k]!="(":
                    try :
                        te+=stack[k]
                    except:
                        print(0)
                        exit(0)
                    stack.pop()
                else:
                    stack[-1]=te*2
                    break
        elif S[i]=="]":
            if not stack:
                print(0)
                exit(0)
            for k in range(len(stack)-1,-1,-1):
                if stack[k]!="[":
                    try :
                        te+=stack[k]
                    except:
                        print(0)
                        exit(0)
                    stack.pop()
                else:
                    stack[-1]=te*3
                    break
        i+=1
for i in stack:
    if type(i) is str:
        print(0)
        exit(0)
print(sum(stack))
    