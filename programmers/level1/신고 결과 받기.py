from collections import defaultdict
def solution(id_list, report, k):
    answer = [0]* len(id_list)
    
    report_dic = defaultdict(int)
    report_set = defaultdict(set)
    for i in report:
        be, af = i.split(" ")
        if af not in report_set[be]:
            report_dic[af]+=1
            report_set[be].add(af)
    black_list =[]
    for id, cnt in report_dic.items():
        if cnt >= k:
            black_list.append(id)
         
    for i in report_set.keys():
        for j in black_list:
            if j in report_set[i]:
                answer[id_list.index(i)]+=1
        
    return answer
id_list = ["con", "ryan"]
report = ["ryan con", "ryan con", "ryan con", "ryan con"]
k = 3
print(solution(id_list,report,k))