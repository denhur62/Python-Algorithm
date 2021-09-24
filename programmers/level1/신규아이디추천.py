def solution(new_id):
    new_id=new_id.lower()
    arr = [i for i in new_id if i.isalpha() or i.isdigit()
        or i=="_" or i=="." or i=="-"]
    i=0
    while i<len(arr):
        if arr[i:i+2]==[".","."]:
            del arr[i]
        else:
            i+=1
    if arr:
        if arr[0]==".":
            arr.pop(0)
        if arr and arr[-1]==".":
            arr.pop()
    if not arr:
        arr.append("a")
    if len(arr)>=16:
        arr=arr[:15]
        if arr[-1]==".":
            arr=arr[:14]
    if len(arr)<=2:
        while len(arr)<=2:
            arr.append(arr[-1])
    return "".join(arr)

a="abcdefghijklmn.p"
print(solution(a))