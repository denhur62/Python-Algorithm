from collections import defaultdict
from math import ceil
def solution(fees, records):
    answer = []
    dic = defaultdict(list)
    for record in records:
        time, car_number, IO = record.split()
        time = time.split(":")
        seconds = int(time[0]) *60 + int(time[1])
        dic[car_number].append(seconds)
    dic = dict(sorted(dic.items()))
    for key in dic.keys():
        record_len = len(dic[key])
        if record_len %2== 1:
            dic[key].append(23*60+59)
        price=0
        time=0
        for i in range(0,record_len,2):
            time+= dic[key][i+1]- dic[key][i]
        if time >=fees[0]:
            price +=fees[1] + ceil((time- fees[0])/fees[2])*fees[3]
        else:
            price += fees[1]
        answer.append(price)
    return answer




fess = [120, 0, 60, 591]
records = ["16:00 3961 IN","16:00 0202 IN","18:00 3961 OUT","18:00 0202 OUT","23:58 3961 IN"]

print(solution(fess, records))


