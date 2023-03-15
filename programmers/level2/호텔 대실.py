from datetime import datetime, timedelta
def solution(book_time):
    real_book_time =[]
    max_time, min_time = datetime.strptime('0000','%H%M'), datetime.strptime('2359','%H%M')
    for i in book_time:
        temp_s, temp_e = i[0].split(':'), i[1].split(':')
        s, e = datetime.strptime(temp_s[0]+temp_s[1],'%H%M'), \
            datetime.strptime(temp_e[0]+temp_e[1],'%H%M')+ timedelta(minutes=10)
        real_book_time.append([s,e])
        if min_time > s:
            min_time = s
        if max_time < e:
            max_time = e
    answer=0
    while min_time <= max_time:
        temp=0
        curr_time = min_time
        for i in real_book_time:
            if i[0]<= curr_time and i[1]> curr_time:
                temp+=1
        if answer < temp:
            answer=temp
        min_time += timedelta(minutes=1)  
    
    return answer


print(solution([["15:00", "17:00"], ["16:40", "18:20"], ["14:20", "15:20"], ["14:10", "19:20"], ["18:20", "21:20"]]))