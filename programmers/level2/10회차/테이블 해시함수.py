def solution(data, col, row_begin, row_end):
    data.sort(key= lambda x:( x[col-1], -x[0]))
    answer=0
    for i in range(row_begin-1,row_end):
        mod_cnt =0
        for j in data[i]:
            mod_cnt += j %(i+1)
        if i == row_begin-1:
            answer+=mod_cnt
        else:
            answer ^= mod_cnt

    return answer


print(solution([[2,2,6],[1,5,10],[4,2,9],[3,8,3]],2,2,3))