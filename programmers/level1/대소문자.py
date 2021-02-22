def solution(s):
    count, count2 = 0, 0
    for i in s:
        if i == 'y' or i == 'Y':
            count += 1
        elif i == 'p' or i == 'P':
            count2 += 1
    if count == count2:
        return True
    else:
        return False
