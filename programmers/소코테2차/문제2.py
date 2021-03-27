from collections import defaultdict
import sys


N,M= map(int,sys.stdin.readline().split())
dic=defaultdict(lambda :[])
for i in range(N-1):
    a,b=map(int,sys.stdin.readline().split())
    dic[a].append(b)
new_dic=defaultdict(lambda :[])
def cycle():
    value=list(dic.keys())
    for i in value:
        stack=[i]
        while stack:
            temp=stack.pop()
            if temp in value:
                for j in dic[temp]:
                    new_dic[i].append(j)
                    stack.append(j)

def list_to_set():
    for i in list(new_dic.keys()):
        new_dic[i]=set(new_dic[i])
    
cycle()
list_to_set()
for i in range(M):
    a,b=map(int,sys.stdin.readline().split())
    if b in new_dic[a]:
        print("yes")
    else:
        print("no")
