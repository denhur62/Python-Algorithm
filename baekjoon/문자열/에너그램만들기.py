from collections import Counter

a=input()
b=input()
temp=sum((Counter(a)&Counter(b)).values())

print(len(a)+len(b)-2*temp)