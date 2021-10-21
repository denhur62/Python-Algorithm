import sys
N , K =map(int,input().split())
words=[]
for i in range(N):
    temp=sys.stdin.readline()
    temp=temp[4:-5]
    words.append(temp)
if K<5:
    print(0)
    exit(0)
if K==26:
    print(N)
    exit(0)

learn=[0]*26
answer=0
def dfs(cnt,idx):
    global answer
    if cnt==K-5:
        temp=0
        for word in words:
            flag=True
            for w in word:
                if learn[ord(w)-ord('a')]==0:
                    flag=False
                    break
            if flag:
                temp+=1
        answer=max(answer,temp)
        return 

    for k in range(idx,26):
        if learn[k]==0:
            learn[k]=1
            dfs(cnt+1,k)
            learn[k]=0
        
    
for i in ('i','a','n','c','t'):
    learn[ord(i)-ord('a')]=1
dfs(0,0)
print(answer)