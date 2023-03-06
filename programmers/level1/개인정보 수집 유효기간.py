
def solution(today, terms, privacies):
    year , month , day = map(int,today.split("."))
    d = year*28*12 + month*28 + day
    
    dic = dict()
    answer = []
    index = 1
    for i in terms:
        key, value = i.split(" ")
        dic[key] = int(value)
    
    for i in privacies:
        lastDay , key = i.split(" ")
        last_year, last_month , last_day = map(int,lastDay.split("."))
        print(last_year*28*12+last_month*28+last_day+ 28*dic[key])
        if d >= last_year*28*12+last_month*28+last_day+ 28*dic[key]:
            answer.append(index)
        index+=1
    
    return answer


today = "2022.05.19"
terms =["A 6", "B 12", "C 3"]
privacies = ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]
print(solution(today,terms,privacies))    